from dcs import mapping
from dcs.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Iraq(Terrain):
    center = {"lat": 30.76, "long": 59.07}
    temperature = [
        (-1, 12),
        (1, 14),
        (4, 18),
        (7, 23),
        (12, 31),
        (18, 38),
        (22, 42),
        (22, 42),
        (17, 37),
        (12, 29),
        (5, 20),
        (2, 14),
    ]
    assert len(temperature) == 12

    def __init__(self):
        super().__init__(
            "Iraq",
            PARAMETERS,
            bounds=mapping.Rectangle(440000, -500000, -950000, 850000, self),
            map_view_default=MapView(mapping.Point(0, 0, self), self, 1000000)
        )
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
