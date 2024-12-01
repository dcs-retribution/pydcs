from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any

from dcs.datalinks.datalinkbase import DataLinkSettings, DataLinkNetwork
from dcs.datalinks.idm import IdmApacheSettings, IdmApacheNetwork
from dcs.datalinks.link16 import Link16HornetSettings, Link16Network, Link16ViperSettings, ViperLink16NetworkMemberLink
from dcs.datalinks.sadl import SadlWarthogIISettings


class DataLinkType(Enum):
    LINK16 = "Link16"
    SADL = "SADL"
    IDM = "IDM"


@dataclass
class DataLink:
    link_type: DataLinkType
    settings: DataLinkSettings
    network: DataLinkNetwork

    def dict(self) -> Dict[str, Any]:
        return {
            self.link_type.value: {
                "settings": self.settings.dict(),
                "network": self.network.dict(),
            }
        }

    @staticmethod
    def for_aircraft_id(ac_id: str) -> DataLink:
        if ac_id == "FA-18C_hornet":
            # Link16 - Hornet
            return DataLink(
                link_type=DataLinkType.LINK16,
                settings=Link16HornetSettings(),
                network=Link16Network(
                    max_members=4,
                    max_donors=8,
                ),
            )
        elif ac_id == "F-16C_50":
            # Link16 - Viper
            return DataLink(
                link_type=DataLinkType.LINK16,
                settings=Link16ViperSettings(),
                network=Link16Network(
                    max_members=8,
                    max_donors=4,
                    member_link_type=ViperLink16NetworkMemberLink,
                ),
            )
        elif ac_id == "A-10C_2":
            # SADL - Warthog II
            return DataLink(
                link_type=DataLinkType.SADL,
                settings=SadlWarthogIISettings(),
                network=Link16Network(
                    max_members=4,
                    max_donors=12,
                ),
            )
        elif ac_id == "AH-64D_BLK_II":
            # IDM - Apache
            return DataLink(
                link_type=DataLinkType.IDM,
                settings=IdmApacheSettings(),
                network=IdmApacheNetwork(),
            )
        else:
            raise RuntimeError(f"Datalink network not supported for aircraft with id '{ac_id}'")
