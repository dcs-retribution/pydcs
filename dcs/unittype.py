from __future__ import annotations

from pathlib import Path

import dcs.lua as lua
from dcs.payloads import PayloadDirectories
import re
import sys
from typing import Any, Dict, Iterator, List, Optional, Set, Type, Union, TYPE_CHECKING

from dcs.liveries.livery import Livery
from dcs.liveries.liverycache import LiveryCache
from .datalinks.datalink import DataLink

if TYPE_CHECKING:
    from dcs.country import Country
    from dcs.task import MainTask
    from .unitpropertydescription import UnitPropertyDescription


class UnitType:
    id: str
    name: str


class VehicleType(UnitType):
    eplrs = False
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class ShipType(UnitType):
    helicopter_num = 0
    plane_num = 0
    parking = 0


class StaticType(UnitType):
    shape_name: str
    rate = 0
    category = "Fortifications"
    sea_object = False
    can_cargo = False
    mass = None


class LiveryOverwrites:
    map = {
        "M-2000C.FRA": "AdA Chasse 2-5"
    }


#: A dict of 1-indexed channel IDs to the preset frequency.
RadioPresets = Dict[int, float]


#: A dict mapping "channels" to the radio channel presets.
RadioConfig = Dict[str, RadioPresets]


#: A dict mapping the 1-indexed radio ID to the radio configuration.
AircraftRadioPresets = Dict[int, RadioConfig]


class FlyingType(UnitType):
    flyable = False
    group_size_max = 4
    large_parking_slot = False
    helicopter = False
    fuel_max: float = 0
    max_speed: float = 500
    height: float = 0
    width: float = 0
    length: float = 0
    ammo_type = None
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Air"

    callnames: Dict[str, List[str]] = {}

    tacan = False
    eplrs = False
    networked_datalink = False

    radio_frequency: float = 251

    #: The preset radio channels for the aircraft, if the aircraft supports them. Not all aircraft support radio presets. Those
    # that don't will have None for their panel_radio.
    panel_radio: Optional[AircraftRadioPresets] = None

    property_defaults: Optional[Dict[str, Any]] = None

    properties: Dict[str, UnitPropertyDescription] = {}

    pylons: Set[int] = set()
    livery_name: Optional[str] = None

    # Dict from payload name to the DCS payload structure. None if not yet initialized.
    payloads: Optional[Dict[str, Dict[str, Any]]] = None

    tasks: List[Union[str, Type["MainTask"]]] = ["Nothing"]
    task_default: Optional[Type["MainTask"]] = None

    _payload_cache = None
    _UnitPayloadGlobals = None

    @classmethod
    def add_to_payload_cache(cls, payload_file: Path):
        if not FlyingType._payload_cache:
            return cls.scan_payload_dir()
        if payload_file not in FlyingType._payload_cache:
            FlyingType._payload_cache[payload_file] = cls.id

    @classmethod
    def scan_payload_dir(cls):
        if FlyingType._payload_cache:
            return
        FlyingType._payload_cache = {}
        for payload_dir in PayloadDirectories.payload_dirs():
            if not payload_dir.exists():
                continue
            for payload_path in payload_dir.glob("*.lua"):
                if payload_path not in FlyingType._payload_cache:
                    with payload_path.open('r', encoding='utf-8') as payload_file:
                        for line in payload_file:
                            g = re.search(r'\["unitType"]\s*=\s*"([^"]*)', line)
                            if g:
                                FlyingType._payload_cache[payload_path] = g.group(1)
                                break

    @classmethod
    def load_payloads(cls):
        # avoid cyclic dependency
        if FlyingType._UnitPayloadGlobals is None:
            from . import task
            FlyingType._UnitPayloadGlobals = {v.internal_name: v.id for k, v in task.MainTask.map.items()}

        FlyingType.scan_payload_dir()
        if cls.payloads is not None:
            return cls.payloads
        cls.payloads = {}

        for payload_dir in PayloadDirectories.payload_dirs():
            if not payload_dir.exists():
                continue
            for payload_path in payload_dir.glob("*.lua"):
                if FlyingType._payload_cache[payload_path] == cls.id and payload_path.exists():
                    try:
                        payload_main = lua.loads(payload_path.read_text(), _globals=FlyingType._UnitPayloadGlobals)
                    except SyntaxError:
                        print("Error parsing lua file '{f}'".format(f=payload_path), file=sys.stderr)
                        raise
                    pays = payload_main["unitPayloads"]
                    if pays["unitType"] == cls.id:
                        for load in pays["payloads"].values():
                            name = load["name"]
                            # Payload directories are iterated in decreasing order of
                            # preference, so if we already have a payload matching the
                            # name, ignore it.
                            if name not in cls.payloads:
                                cls.payloads[load["name"]] = load

        return cls.payloads

    @classmethod
    def loadout(cls, _task):
        if cls.payloads is not None:
            for payload in cls.payloads.values():
                tasks = [payload["tasks"][x] for x in payload["tasks"]]
                if _task.id in tasks:
                    pylons = payload["pylons"]
                    r = [(pylons[x]["num"], {"clsid": pylons[x]["CLSID"]}) for x in pylons]
                    return r
        return None

    @classmethod
    def loadout_by_name(cls, loadout_name):
        if cls.payloads is not None:
            payload = cls.payloads.get(loadout_name)
            if payload is None:
                return None
            pylons = payload["pylons"]
            r = [(pylons[x]["num"], {"clsid": pylons[x]["CLSID"]}) for x in pylons]
            return r
        return None

    @classmethod
    def iter_liveries(cls) -> Iterator[Livery]:
        if cls.livery_name is None:
            return
        yield from LiveryCache.for_unit(cls.livery_name)

    @classmethod
    def iter_liveries_for_country(cls, country: Country) -> Iterator[Livery]:
        if cls.livery_name is None:
            return
        for livery in LiveryCache.for_unit(cls.livery_name):
            if livery.valid_for_country(country.shortname):
                yield livery

    @classmethod
    def default_livery(cls, country_name) -> str:
        if cls.id + "." + country_name in LiveryOverwrites.map:
            return LiveryOverwrites.map[cls.id + "." + country_name]
        else:
            liveries = sorted(
                livery
                for livery in cls.iter_liveries()
                if livery.valid_for_country(country_name)
            )
            if liveries:
                return liveries[0].id
        return ""

    @classmethod
    def get_default_datalink(cls) -> Optional[DataLink]:
        if cls.networked_datalink:
            return DataLink.for_aircraft_id(cls.id)
        return None

    @classmethod
    def is_link16_capable(cls) -> bool:
        # i.e. can be added as team-member/donor for L16
        return "STN_L16" in cls.properties

    @classmethod
    def is_sadl_capable(cls) -> bool:
        # i.e. can be added as team-member/donor for SADL
        return "SADL_TN" in cls.properties

    @classmethod
    def is_idm_capable(cls) -> bool:
        # i.e. can be added as team-member for IDM
        return "TN_IDM_LB" in cls.properties

    @classmethod
    def datalink_networkable(cls) -> bool:
        return cls.is_link16_capable() or cls.is_sadl_capable() or cls.is_idm_capable()
