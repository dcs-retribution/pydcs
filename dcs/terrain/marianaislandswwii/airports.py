# flake8: noqa
from typing import List, Type

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


class Agana(Airport):
    id = 1
    name = "Agana"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3800000, vhf_low_hz=38500000, vhf_high_hz=118100000, uhf_hz=250100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-265.031212, -855.033463, terrain), terrain)

        self.runways.append(Runway(id=1, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-590.26763916016, -1909.0552978516, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-778.11981201172, -1110.3016357422, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-749.93011474609, -1058.544921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-234.37846374512, -139.57736206055, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-119.6450881958, -188.38691711426, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-143.29655456543, -239.57627868652, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-166.81954956055, -321.89639282227, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-548.44543457031, -870.09649658203, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-511.01617431641, -808.28436279297, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-612.53063964844, -1014.8760375977, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-679.04632568359, -1873.1959228516, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-590.61145019531, -1816.591796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-671.04083251953, -1824.8472900391, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-698.35540771484, -1724.4947509766, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-708.21862792969, -1950.5599365234, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-768.48303222656, -1259.9460449219, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-847.431640625, -1327.7749023438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-812.28308105469, -1372.4099121094, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-678.95581054688, -1369.0699462891, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-722.18811035156, -1419.5015869141, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-861.54302978516, -1447.3106689453, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-819.75384521484, -1545.4951171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-860.95684814453, -1600.0538330078, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-881.30676269531, -1697.2312011719, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-969.76434326172, -1668.7613525391, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-871.33660888672, -1860.3433837891, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-879.59338378906, -1876.1312255859, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-935.80682373047, -1873.2894287109, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-818.75512695312, -1929.7283935547, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-796.81713867188, -1916.7852783203, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-888.74322509766, -1891.8813476562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-784.07165527344, -1939.7183837891, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-762.55297851562, -1925.8316650391, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-952.42633056641, -1779.6759033203, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-842.48443603516, -1857.7563476562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-782.62677001953, -1695.0241699219, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-834.32415771484, -1679.6951904297, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-755.64886474609, -1619.5570068359, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-810.80200195312, -1606.0892333984, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))


class Orote(Airport):
    id = 2
    name = "Orote"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=118150000, uhf_hz=250150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-5113.726, -17192.351926, terrain), terrain)

        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-5152.4877929688, -17435.439453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-5200.7622070312, -17414.365234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-5318.1899414062, -17269.248046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-5338.033203125, -17349.13671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-5229.1171875, -17362.923828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-5246.7143554688, -17397.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-5204.3837890625, -17339.54296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-5043.271484375, -16875.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-5037.9624023438, -16903.505859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-5305.5307617188, -17196.51171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-5279.3642578125, -17131.72265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-5441.8237304688, -17327.556640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-5434.4418945312, -17292.001953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-5428.7841796875, -17257.662109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-5422.33984375, -17221.990234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-5416.6948242188, -17190.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-5411.8330078125, -17157.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-5407.072265625, -17125.13671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-5372.3413085938, -17068.599609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-5352.2509765625, -17036.978515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-5338.66015625, -17005.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-5023.3100585938, -16946.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-5030.3461914062, -16924.787109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-5003.203125, -17036.30078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-5009.7543945312, -17014.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-5009.0703125, -16991.126953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-5015.62109375, -16969.224609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-4958.5478515625, -17166.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-4962.1669921875, -17143.16015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-4985.0151367188, -17102.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-4983.4428710938, -17076.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-4968.7177734375, -17121.255859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-4991.0590820312, -17055.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))


class Airfield_3(Airport):
    id = 3
    name = "Airfield 3"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=118200000, uhf_hz=250200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(174464.570313, 91676.0625, terrain), terrain)

        self.runways.append(Runway(id=1, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(174439.0625, 91148.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(174381.96875, 91166.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(174322.84375, 91236.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(174302.015625, 91285.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(174297.640625, 91333.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(174250.1875, 91129.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(174219.03125, 91182.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(174199.859375, 91240.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(174188.578125, 91299.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(174188.09375, 91360.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(174195.328125, 91420.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(174211.1875, 91478.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(174234.875, 91535.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(174371.640625, 91699.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(174340.03125, 91725.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(174311.09375, 91754.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(174288.0625, 91791.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(174272.4375, 91831.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(174263.859375, 91870.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(174260.96875, 91915.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(174260.046875, 91956.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(174262.078125, 91998.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(174267.765625, 92041.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(174279.640625, 92083.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(174295.34375, 92123.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(174459.859375, 91262.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(174429.203125, 91287.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(174405.359375, 91319.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(174389.546875, 91356.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(174383.25, 91396.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(174383.5625, 91436.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(174390.421875, 91477.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(174403.4375, 91517.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(174621.546875, 91231.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(174617.9375, 91256.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(174615.125, 91281.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(174611.75, 91306.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(174608.15625, 91331.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(174605.328125, 91356.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(174587.78125, 91499.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(174584.171875, 91524.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(174581.359375, 91549.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(174591.140625, 91473.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(174593.96875, 91448.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(174597.5625, 91423.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(174562.109375, 91710.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(174558.515625, 91735.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(174555.6875, 91760.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(174565.484375, 91684.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(174568.296875, 91659.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(174571.890625, 91634.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(174541.75, 91862.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(174538.15625, 91887.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(174535.328125, 91912.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(174545.125, 91837.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(174547.9375, 91812.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(174551.546875, 91787.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(174531.765625, 91938.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(174528.953125, 91963.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(174513.90625, 92097.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(174510.3125, 92121.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(174507.484375, 92147.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(174517.28125, 92071.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(174520.09375, 92046.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(174523.703125, 92021.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(174267.046875, 91651.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(174237.484375, 91682.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(174211.1875, 91720.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(174191.84375, 91760.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(174178.1875, 91802.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(174169.59375, 91846.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(174164.703125, 91889.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(174163.34375, 91930.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(174164.3125, 91973.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(174195.6875, 92120.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(174178.703125, 92068.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(174170.390625, 92017.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(174304.1875, 91378.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(174306.9375, 91419.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(174272.015625, 91578.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(174306.53125, 91591.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))


class Charon_Kanoa(Airport):
    id = 4
    name = "Charon Kanoa"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=38650000, vhf_high_hz=118250000, uhf_hz=250250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(184643.730455, 99390.186705, terrain), terrain)

        self.runways.append(Runway(id=1, name='03-21', main=RunwayApproach(name='03', heading=30, beacons=[]), opposite=RunwayApproach(name='21', heading=210, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(185119.50969051, 99799.748916704, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(185106.17878302, 99828.64518614, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(185088.75709523, 99854.919754117, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(185051.94555537, 99869.842031135, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(185023.79621124, 99861.461284632, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(184925.19967026, 99701.144208556, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(184962.20901871, 99746.059202188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(184906.90625832, 99643.688915113, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(185002.49681857, 99825.448504146, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(184980.3842146, 99806.795236303, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(185015.03895733, 99760.178118521, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(185038.58596651, 99772.420785632, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))


class Gurguan_Point(Airport):
    id = 5
    name = "Gurguan Point"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3900000, vhf_low_hz=38700000, vhf_high_hz=118300000, uhf_hz=250300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(167172.148438, 87766.527344, terrain), terrain)

        self.runways.append(Runway(id=1, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(167289.59375, 87065.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(167320.078125, 87123.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(167332.984375, 87185.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(167322.828125, 88438.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(167272.515625, 88439.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(167272.015625, 88330.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(167322.328125, 88329.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(167006.359375, 87053.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(166920.984375, 87066.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(166817.046875, 87185.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(166714.296875, 87268.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(166654.53125, 87466.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(166725.0625, 87564.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(166674.65625, 87683.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(166791.703125, 87731.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(166924.75, 87833.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(166926.5, 88002.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(166925.203125, 88062.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(166927.265625, 88110.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(166925.96875, 88170.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(166925.046875, 88215.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(166927.96875, 88248.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(166920.625, 88285.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(166928.640625, 88329.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(166938.515625, 88361.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(167132.328125, 87261.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(167136.875, 87240.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(167136.53125, 87218.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(167137.78125, 87195.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(167136.546875, 87173.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(167138.484375, 87150.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(167138.90625, 87125.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(167136.015625, 87103.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(167136.75, 87083.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(167254.453125, 87003.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(167105.34375, 88378.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(167109.890625, 88356.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(167109.546875, 88335.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(167110.78125, 88312.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(167109.5625, 88290.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(167111.5, 88267.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))


class Isley(Airport):
    id = 6
    name = "Isley"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38750000, vhf_high_hz=118350000, uhf_hz=250350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(180112.398438, 101538.226563, terrain), terrain)

        self.runways.append(Runway(id=1, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(180229.234375, 101614.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(180215.34375, 102063.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(180216.265625, 102112.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(180215.640625, 102000.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(180217.25, 101967.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(180221.40625, 101929.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(180219.625, 101892.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(180219.984375, 101856.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(180233.09375, 101817.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(180235.5625, 101669.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(180233.421875, 101748.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(180398.984375, 101348.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(180342.078125, 101341.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(180284.90625, 101340.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(180312.140625, 101340.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(180395.859375, 101510.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(180456.03125, 101527.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(180405.1875, 101385.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(180404.375, 101412.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(180498.9375, 101528.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(180361.625, 101538.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(180361.171875, 101563.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(180362.8125, 101588, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(180309.546875, 101538.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(180313.53125, 101580.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(180320.390625, 101631.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(180321.25, 101656.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(180322.015625, 101681.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(180323.859375, 101703.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(180325.3125, 101726.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(180249.28125, 101026.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(180249.375, 101130.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(180247.796875, 101188.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(180251.390625, 101247.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(180251.21875, 101280.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(180253.203125, 101313.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(180251.578125, 101349.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(180034.265625, 100910.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(180001.78125, 100910.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(179972.1875, 100898.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(179945.84375, 101035.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(180001.046875, 101056.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(180005.671875, 101090.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(179930.421875, 101006.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(180001.375, 101123.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(179919.765625, 100973.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(179997.859375, 101171.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(179901.78125, 100940.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(179996, 101325.3046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(179998.703125, 101237.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(179978.015625, 102084.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(179994.15625, 101428.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(179991.46875, 101611.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(179976.203125, 101790.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(179980.828125, 101824.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(179976.53125, 101857.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(179975.09375, 101895.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(179972.96875, 101932.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(179977.59375, 101967.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(179973.28125, 102000.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(179971.84375, 102038.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(179981.9375, 101755.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(179983.046875, 101724.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(179983.59375, 101692.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))


class Kagman(Airport):
    id = 7
    name = "Kagman"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3950000, vhf_low_hz=38800000, vhf_high_hz=118400000, uhf_hz=250400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(185395.859375, 106655.921875, terrain), terrain)

        self.runways.append(Runway(id=1, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(185181.625, 106204.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(185208.0625, 106253.3046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(185235.3125, 106301.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(185244.390625, 106363.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(185263.484375, 106414.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(185459.125, 107083.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(185513.6875, 107091.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(185555.703125, 107126.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(185323.796875, 106182.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(185323.625, 106215.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(185449.859375, 106135.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(185449.5625, 106101.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(185449.734375, 106067.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(185315.953125, 105991.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(185312.609375, 106030.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(185318.234375, 106066.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(185318.53125, 105894.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(185319.796875, 105925.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(185321.078125, 105956.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(185443.078125, 106018.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(185435.765625, 105995.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(185320.625, 105865.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(185321.03125, 105841.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(185324.84375, 107243.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(185324.375, 107266.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(185324.578125, 107288.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(185324.3125, 107311.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(185322.75, 107334.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(185323.546875, 107360.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(185445.0625, 107272.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(185445.46875, 107302.8359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(185444.25, 107333.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(185443.125, 107362.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))


class Marpi(Airport):
    id = 8
    name = "Marpi"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3975000, vhf_low_hz=38850000, vhf_high_hz=118450000, uhf_hz=250450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(197999.429688, 110912.125, terrain), terrain)

        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(198246.421875, 110462.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(197992.4375, 110582.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(197963.09375, 110634.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(197937.828125, 110684.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(197912.65625, 110732.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(197842.265625, 110883.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(197867.890625, 110834.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(197890.359375, 110783.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(198005.578125, 110116.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(198015.53125, 110175.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(198060.8125, 110203.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(198013.390625, 110236.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(197996.375, 110290.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(197971.90625, 110337.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(197938.28125, 110388.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(198016.0625, 110405.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(197967.109375, 110530.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(198033.390625, 110516.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(197865.640625, 110617.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(197840.78125, 110655.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(197802.0625, 110705.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(197780.984375, 110738.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(197763.03125, 110771.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(197749.0625, 110806.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(197735.0625, 110839.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(197717.75, 110871.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(197770.6875, 110944.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(197799.375, 110964.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(197829.640625, 110984.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(197792.34375, 111077.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(197765.90625, 111059.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(197735.234375, 111038.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(197698.9375, 111012.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(197671.21875, 110984.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(197651.515625, 110944.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))


class Rota(Airport):
    id = 9
    name = "Rota"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4000000, vhf_low_hz=38900000, vhf_high_hz=118500000, uhf_hz=250500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(75890.574219, 48691.287109, terrain), terrain)

        self.runways.append(Runway(id=1, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(75660.9375, 48937.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(75660.1796875, 48706.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(76194.671875, 48126.25390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(76290.078125, 48006.83203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(76307.03125, 48248.61328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(76019.34375, 49018.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(76104.859375, 49129.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(75602.15625, 49252.89453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(75601.859375, 49397.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(75780.4609375, 48955.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(75989.0234375, 48608.18359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(76216.8046875, 48409.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(76249.171875, 48300.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(76121.9296875, 48358.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(76057.3515625, 48371.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(76024.9921875, 48358.78515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(75990.5546875, 48579.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(75991.6015625, 48552.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(75992.640625, 48523.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(75698.6953125, 48044.41015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(75994.375, 48493.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(75995.6484375, 48465.87109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(75784.9765625, 48865.57421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(75783.2890625, 48896.42578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(75782.578125, 48924.83203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(75751.8984375, 48827.91015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(76066.546875, 48090.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(76378.1171875, 48052.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(76403.078125, 48159.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(76397.8671875, 48245.64453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(76141.4765625, 47998.67578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(76368.3515625, 48337.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(76409.5234375, 48494.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(76185.171875, 48826.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(76240.0546875, 48825.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(76090.8984375, 48936.47265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(75985.75, 49284.28515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(76070.5546875, 49284.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(75767.984375, 47925.03515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(75660.203125, 47932.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(75466.9140625, 47933.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(75608.0078125, 48019.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(75521.65625, 48052.16015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(75477.0390625, 48033.71484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(75413.140625, 48078.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(75421.2421875, 48132.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(75382.703125, 48384.96484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(75476.875, 48491.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(75412.375, 48553.71484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(75588.8515625, 48802.17578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(75501.84375, 48855.61328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(75481.5078125, 48777.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=11.0, shelter=False))


class Ushi(Airport):
    id = 10
    name = "Ushi"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3750000, vhf_low_hz=38400000, vhf_high_hz=118000000, uhf_hz=250000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(175590.500003, 91892.848195, terrain), terrain)

        self.runways.append(Runway(id=1, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(175207.375, 92330.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(175222.8125, 92385.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(175241.578125, 92440.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(175272.546875, 92494.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(175368.578125, 92559.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(175300.859375, 92069.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(175368.25, 91989.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(175417.40625, 91842.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(175425.046875, 91780.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(175903.140625, 91386.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(175920.828125, 91438.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(175950.171875, 91484.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(175955.609375, 91539.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(175882.1875, 92415.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(175853.953125, 92473.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(175832.3125, 92532.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(175783.625, 92612.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(175409.671875, 92116.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(175405.265625, 92153.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(175404.703125, 92212.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(175400.640625, 92249.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(175390.6875, 92288.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(175385.359375, 92329.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(175387.3125, 92369.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(175380.671875, 92408.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(175472.265625, 92275.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(175470.6875, 92231.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(175486.78125, 92077.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(175600.578125, 92616.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(175713.359375, 92500.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(175725.765625, 92467.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(175736.765625, 92439.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(175750.625, 92406.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(175774.015625, 92344.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(175785.796875, 92313.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(175645.46875, 92456.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(175672.46875, 92393.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(175687.03125, 92362.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(175700.171875, 92334.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(175728.859375, 92262, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(175741.484375, 92230.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(175744.3125, 92191.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(175329.75, 92236.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(175325.578125, 92273.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(175321.078125, 92311.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(175474.75, 92190.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(175461.546875, 92320.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(175458.46875, 92356.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(175457.046875, 92394.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(175450.65625, 92438.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(175677.734375, 91809.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(175674.984375, 91834.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(175672.375, 91859.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(175670.203125, 91886.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(175665.1875, 91914.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(175664.4375, 91948.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(175661.765625, 91978.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(175659.171875, 92006.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(175649.78125, 92084.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(175650.078125, 92114.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(175645.75, 92144.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(175644.125, 92176.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(175640.34375, 92209.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(175638.71875, 92237.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(175720.875, 91876.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(175722.375, 91851.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(175725.359375, 91828.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(175718.21875, 91935.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(175711.203125, 92022.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(175713.53125, 91995.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(175715.8125, 91968.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(175698.296875, 92163.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(175701.5, 92134.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(175703.5, 92101.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(175695.5625, 92228.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(175698.765625, 92200.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(175724.125, 91666.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(175719.84375, 91638.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(175713.46875, 91606.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(175731.375, 91732.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(175729, 91703.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(175512.375, 91808.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(175520.578125, 91770.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(175519.203125, 91738.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(175521.515625, 91706.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(175526.015625, 91673.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(175528.21875, 91645.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(175804.328125, 91452.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(175825.75, 91505.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(175849.4375, 91556.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(175723.078125, 91447.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(175746.515625, 91511.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(175768.671875, 91563.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(175796.09375, 91626.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(175769.234375, 91836.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(175765.15625, 91874.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(175762.84375, 91908.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(175759.453125, 91945.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(175756.828125, 91980.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(175754.578125, 92015.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(175759.3125, 92056.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(175764.34375, 92090.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(175809.84375, 91657.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))


class Pagan(Airport):
    id = 11
    name = "Pagan"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3775000, vhf_low_hz=38450000, vhf_high_hz=118050000, uhf_hz=250050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(512458.328125, 107751.828125, terrain), terrain)

        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(512334.96875, 107622.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(512309.375, 107619.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(512229.1875, 107774.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(512249.1875, 107782.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(512275.9375, 107785.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(512303.625, 107783.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(512260.75, 107610.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(512283.96875, 107613.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(512570.3125, 107611.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(512577.375, 107582.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(512582.15625, 107552.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(512566.25, 107639.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(512558.78125, 107671.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(512553.6875, 107707.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(512505.4375, 107915.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(512512.46875, 107886.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(512517.25, 107856.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(512501.34375, 107943.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(512493.90625, 107975.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))


ALL_AIRPORTS: List[Type[Airport]] = [
    Agana,
    Orote,
    Airfield_3,
    Charon_Kanoa,
    Gurguan_Point,
    Isley,
    Kagman,
    Marpi,
    Rota,
    Ushi,
    Pagan,
]

