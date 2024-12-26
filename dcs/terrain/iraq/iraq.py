from dcs import mapping
from dcs.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Iraq(Terrain):
    center = {"lat": 30.76, "long": 59.07}
    temperature = [
        (5, 16),
        (6, 19),
        (10, 24),
        (16, 30),
        (21, 37),
        (25, 42),
        (27, 45),
        (26, 44),
        (22, 40),
        (17, 34),
        (10, 24),
        (6, 18),
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
