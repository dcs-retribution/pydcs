from dataclasses import dataclass, field
from typing import Dict, Any, Type

from dcs.datalinks.datalinkbase import DataLinkSettings, DataLinkNetwork, DataLinkNetworkLink, \
    DataLinkSettingsWithFlightLead


@dataclass
class Link16Network(DataLinkNetwork):
    max_members: int
    max_donors: int
    team_members: list[DataLinkNetworkLink] = field(default_factory=list)
    donors: list[DataLinkNetworkLink] = field(default_factory=list)
    member_link_type: Type = DataLinkNetworkLink
    donor_link_type: Type = DataLinkNetworkLink

    def dict(self) -> Dict[str, Any]:
        return {
            "teamMembers": {
                i: member.dict()
                for i, member in enumerate(self.team_members, 1)
            },
            "donors": {
                i: donor.dict()
                for i, donor in enumerate(self.donors, 1)
            },
        }

    def add_member(self, unit_id: int) -> bool:
        if len(self.team_members) < self.max_members:
            self.team_members.append(self.member_link_type(unit_id))
            return True
        return False

    @property
    def has_donors(self) -> bool:
        return True

    def add_donor(self, unit_id: int) -> bool:
        if len(self.donors) < self.max_donors:
            self.donors.append(self.donor_link_type(unit_id))
            return True
        return False


@dataclass
class Link16HornetSettings(DataLinkSettings):
    ff1_channel: int = 2
    ff2_channel: int = 3
    transmit_power: int = 0
    aic_channel: int = 1
    voca_channel: int = 4
    vocb_channel: int = 5

    def dict(self) -> Dict[str, Any]:
        return {
            "FF1_Channel": self.ff1_channel,
            "FF2_Channel": self.ff2_channel,
            "transmitPower": self.transmit_power,
            "AIC_Channel": self.aic_channel,
            "VOCA_Channel": self.voca_channel,
            "VOCB_Channel": self.vocb_channel,
        }


@dataclass
class Link16ViperSettings(DataLinkSettingsWithFlightLead):
    transmit_power: int = 3
    special_channel: int = 1
    fighter_channel: int = 1
    mission_channel: int = 1

    def dict(self) -> Dict[str, Any]:
        return {
            "flightLead": self.flight_lead,
            "transmitPower": self.transmit_power,
            "specialChannel": self.special_channel,
            "fighterChannel": self.fighter_channel,
            "missionChannel": self.mission_channel,
        }


@dataclass
class ViperLink16NetworkMemberLink(DataLinkNetworkLink):
    tdoa: bool = False

    def dict(self) -> Dict[str, Any]:
        d = super().dict()
        d["TDOA"] = self.tdoa
        return d
