from dcs import mapping
from dcs.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class GermanyColdWar(Terrain):
    center = {"lat": 52.468, "long": 59.173}
    temperature = [
        # From Berlin's Wikipedia page
        (-2, 3),
        (-2, 5),
        (0, 9),
        (4, 15),
        (8, 20),
        (12, 23),
        (14, 25),
        (14, 25),
        (10, 20),
        (6, 14),
        (2, 8),
        (-1, 4),
    ]
    assert len(temperature) == 12

    def __init__(self):
        super().__init__(
            "GermanyCW",
            PARAMETERS,
            # bounds from approximate bounds in MissionEditor (placing units at borders)
            bounds=mapping.Rectangle(-425000.0, -600000.0, -1100000.0, 260000.0, self),
            map_view_default=MapView(mapping.Point(0, 0, self), self, 1000000),
        )
        self.bullseye_blue = {"x": -384, "y": -781}
        self.bullseye_red = {"x": -384, "y": -781}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
