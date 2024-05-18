import dcs.mapping as mapping
from dcs.terrain.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Kola(Terrain):
    center = {"lat": 68.0, "long": 22.5}
    temperature = [
        (-15, -9),
        (-14, -8),
        (-11, -3),
        (-5, 1),
        (1, 8),
        (7, 15),
        (10, 19),
        (8, 16),
        (4, 11),
        (-2, 2),
        (-7, -3),
        (-11, -6)
    ]
    assert len(temperature) == 12

    def __init__(self):
        bounds = mapping.Rectangle(-315000, -890000, 900000, 856000, self)
        super().__init__(
            "Kola",
            PARAMETERS,
            bounds,
            map_view_default=MapView(bounds.center(), self, 1000000)
        )
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
