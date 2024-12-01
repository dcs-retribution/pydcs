from dataclasses import dataclass
from typing import Dict, Any

from dcs.datalinks.datalinkbase import DataLinkSettingsWithFlightLead


@dataclass
class SadlWarthogIISettings(DataLinkSettingsWithFlightLead):
    air_key: int = 10
    gateway_key: int = 8

    def dict(self) -> Dict[str, Any]:
        return {
            "flightLead": self.flight_lead,
            "AirKey": self.air_key,
            "GatewayKey": self.gateway_key,
        }
