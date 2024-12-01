from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Any


class DataLinkBase(ABC):
    @abstractmethod
    def dict(self) -> Dict[str, Any]:
        ...


class DataLinkSettings(DataLinkBase, ABC):
    pass


class DataLinkSettingsWithFlightLead(DataLinkSettings, ABC):
    flight_lead: bool = False


class DataLinkNetwork(DataLinkBase, ABC):
    @abstractmethod
    def add_member(self, unit_id: int) -> bool:
        ...

    @property
    def has_donors(self) -> bool:
        return False

    def add_donor(self, unit_id: int) -> bool:
        raise RuntimeError(f"'add_donor' not supported for datalink network type: {type(self)}")


@dataclass
class DataLinkNetworkLink(DataLinkBase):
    mission_unit_id: int

    def dict(self) -> Dict[str, Any]:
        return {
            "missionUnitId": self.mission_unit_id,
        }
