# flake8: noqa
"""PLACEHOLDER -- not yet exported from DCS.

Regenerate this file, do not hand-write it:

    tools/airport_import.py -t marianaislandswwii C:\standlist.lua

See the docstring at the top of tools/airport_import.py for how to produce
standlist.lua from the Mission Editor. The terrain ships 11 airfields, whose
ids follow their radio.lua radioIds (airfieldN_0 -> id N):

    1 Agana Airfield (Guam)          7 Kagman Point Airfield (Saipan)
    2 Orote Airfield (Guam)          8 Marpi Point Strip (Saipan)
    3 Airfield 3 (Guam)              9 Rota Airfield (Rota)
    4 Charon Kanoa Strip (Saipan)   10 Ushi Point Airfield (Tinian)
    5 Gurguan Point Airfield (Tinian) 11 Pagan Airstrip (Pagan)
    6 Isley Field (Saipan)

Until the export runs the terrain loads with no airfields, which is enough to
exercise the theater wiring but not to generate a mission.
"""
from typing import List, Type

from dcs.terrain import Airport


ALL_AIRPORTS: List[Type[Airport]] = []
