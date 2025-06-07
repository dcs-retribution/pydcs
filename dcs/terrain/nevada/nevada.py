# flake8: noqa
from dcs.terrain import Terrain, MapView, Graph
import dcs.mapping as mapping
import os
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Nevada(Terrain):
    center = {"lat": 39.81806, "long": -114.73333}
    temperature = [
        (0, 10),
        (2, 16),
        (6, 22),
        (10, 24),
        (14, 28),
        (19, 35),
        (23, 40),
        (22, 38),
        (18, 33),
        (11, 26),
        (5, 19),
        (1, 13)
    ]
    assert len(temperature) == 12

    def __init__(self):
        bounds = mapping.Rectangle(-167000.0, -330000.0, -500000.0, 210000.0, self)
        super().__init__(
            "Nevada",
            PARAMETERS,
            bounds=bounds,
            map_view_default=MapView(bounds.center(), self, 1000000)
        )
        # nttr center MGRS
        # 11SPE9400410022
        self.bullseye_blue = {"x": -409931.344, "y": -14024.097}
        self.bullseye_red = {"x": -288293.969, "y": -88022.641}

        try:
            self.city_graph = Graph.from_pickle(os.path.join(os.path.dirname(__file__), 'nevada.p'))  # type: Graph
        except FileNotFoundError:
            pass

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
