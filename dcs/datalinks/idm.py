from dataclasses import dataclass, field
from typing import Dict, Any

from dcs.datalinks.datalinkbase import DataLinkSettings, DataLinkNetwork, DataLinkNetworkLink


@dataclass
class IdmApacheSettingsPreset(DataLinkSettings):
    preset_name: str = "PRESET X"
    callsign: str = "PRE X"
    primary_freq: int = 0
    no_acknowledgemnent_retries: int = 2
    lb_net: bool = True
    auto_acknowledgement: bool = True

    def dict(self) -> Dict[str, Any]:
        return {
            "primaryFreq": self.primary_freq,
            "NoAcknowledgmentRetries": self.no_acknowledgemnent_retries,
            "LB_Net": self.lb_net,
            "presetName": self.preset_name,
            "callSign": self.callsign,
            "autoAcknowledgment": self.auto_acknowledgement,
        }


@dataclass
class IdmApacheSettings(DataLinkSettings):
    presets: list[IdmApacheSettingsPreset] = field(default_factory=list)

    def __post_init__(self):
        self.presets = self.default_presets()

    def dict(self) -> Dict[str, Any]:
        return {
            "presets": {
                i: preset.dict()
                for i, preset in enumerate(self.presets, 1)
            }
        }

    @staticmethod
    def default_presets() -> list[IdmApacheSettingsPreset]:
        return [
            IdmApacheSettingsPreset(
                preset_name=f"PRESET {i + 1}",
                callsign=f"PRE {i + 1}" if i < 9 else f"PRE{i + 1}",
                primary_freq=(i + 1) if i < 4 else 0
            )
            for i in range(10)
        ]


@dataclass
class IdmApacheNetworkMember(DataLinkNetworkLink):
    pri_value: bool = True
    tm_value: bool = True

    def dict(self) -> Dict[str, Any]:
        d = super(IdmApacheNetworkMember, self).dict()
        d["PRI_value"] = self.pri_value
        d["TM_value"] = self.tm_value
        return d


@dataclass
class IdmApacheNetworkPreset:
    members: list[IdmApacheNetworkMember] = field(default_factory=list)

    def dict(self) -> Dict[str, Any]:
        return {
            "members": {
                i: member.dict()
                for i, member in enumerate(self.members, 1)
            }
        }


@dataclass
class IdmApacheNetwork(DataLinkNetwork):
    presets: list[IdmApacheNetworkPreset] = field(default_factory=list)

    def __post_init__(self):
        self.presets = [
            IdmApacheNetworkPreset()
            for _ in range(10)
        ]

    def dict(self) -> Dict[str, Any]:
        return {
            "presets": {
                i: preset.dict()
                for i, preset in enumerate(self.presets, 1)
            }
        }

    def add_member(self, unit_id: int) -> bool:
        for preset in self.presets:
            count = len(preset.members)
            if count < 16:
                preset.members.append(
                    IdmApacheNetworkMember(unit_id, pri_value=count <= 8)
                )
            else:
                return False
        return True
