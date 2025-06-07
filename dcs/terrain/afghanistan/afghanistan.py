from dcs import mapping
from dcs.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Afghanistan(Terrain):
    center = {"lat": 33.9346, "long": 66.24705}
    temperature = [
        (-5, 6),
        (-3, 8),
        (2, 14),
        (7, 21),
        (11, 26),
        (23, 31),
        (18, 33),
        (16, 32),
        (11, 28),
        (5, 22),
        (0, 14),
        (-4, 9)
    ]
    assert len(temperature) == 12

    def __init__(self):
        bounds = mapping.Rectangle(532000.0, -534000.0, -512000.0, 757000.0, self)
        super().__init__(
            "Afghanistan",
            PARAMETERS,
            bounds=bounds,
            map_view_default=MapView(bounds.center(), self, 1000000)
        )
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
