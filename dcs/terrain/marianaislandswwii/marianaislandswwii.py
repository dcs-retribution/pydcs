import dcs.mapping as mapping
from dcs.terrain.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class MarianaIslandsWWII(Terrain):
    # Same archipelago as MarianaIslands, so the climate table is shared.
    # https://en.wikipedia.org/wiki/Guam#Climate
    center = {"lat": 13.485, "long": 144.798}
    temperature = [
        (24, 30),
        (24, 30),
        (24, 30),
        (25, 31),
        (25, 31),
        (25, 31),
        (25, 31),
        (25, 30),
        (25, 30),
        (25, 30),
        (25, 30),
        (25, 30)
    ]

    assert len(temperature) == 12

    def __init__(self):
        # From the terrain's own MissionGenerator/nodesMap.lua nodesMapBorders,
        # which is byte-identical to MarianaIslands' -- the two terrains share a
        # coordinate grid.
        bounds = mapping.Rectangle(1096283.375, -1072729.625, -296316.65625, 1252670.375, self)
        super().__init__(
            "MarianaIslandsWWII",
            PARAMETERS,
            bounds,
            # Not bounds.center(): the box spans the whole archipelago, whose
            # centre is open ocean ~400 km north of Saipan. Rota sits midway
            # between Guam and Saipan, where every campaign is fought.
            map_view_default=MapView(mapping.Point(76432, 48051, self), self, 1000000)
        )
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
