import dcs.mapping as mapping
from dcs.terrain.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Sinai(Terrain):
    center = {"lat": 30.047, "long": 31.224}
    temperature = [
        (10, 20),
        (12, 22),
        (15, 25),
        (19, 29),
        (22, 32),
        (25, 35),
        (28, 38),
        (29, 39),
        (27, 37),
        (23, 33),
        (19, 29),
        (15, 24)
    ]
    assert len(temperature) == 12

    def __init__(self):
        bounds = mapping.Rectangle(-450000, -280000, 500000, 560000, self)
        super().__init__(
            "SinaiMap",
            PARAMETERS,
            bounds,
            map_view_default=MapView(bounds.center(), self, 1000000)
        )
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
