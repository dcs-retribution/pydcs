# flake8: noqa
from typing import List, Type

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


class Banak(Airport):
    id = 1
    name = "Banak"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=38650000, vhf_high_hz=118050000, uhf_hz=250200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(234850.039062, 88378.335938, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield1_2'))
        self.beacons.append(AirportBeacon(id='airfield1_3'))
        self.runways.append(Runway(id=1, name='34-16', main=RunwayApproach(name='34', heading=340, beacons=[]), opposite=RunwayApproach(name='16', heading=160, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(233864.84375, 88349.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(233847.78125, 88352.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(233830.71875, 88354.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(233813.59375, 88357.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(233796.28125, 88359.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(233779.109375, 88362.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(233762.171875, 88364.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(233745.09375, 88367.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(233728.203125, 88369.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(233710.984375, 88371.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(233694.109375, 88374.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(233677.1875, 88376.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(233660.0625, 88379.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(233642.328125, 88381.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(233625.125, 88384.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(233607.953125, 88386.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(233590.71875, 88389.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(233635.8125, 88251.3671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HC1', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(233698.5625, 88078.9140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='M20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(233680.34375, 88110.3984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='M19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(233661.15625, 88141.453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='M18', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(234597.75, 88657.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='CIV02', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(234642.9375, 88650.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='CIV03', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(234552.1875, 88664.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='CIV01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(233592.84375, 88164.0078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(233566.046875, 88208.6484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M18', length=21.0, width=15.0, height=8.0, shelter=False))


class Rovaniemi(Airport):
    id = 2
    name = "Rovaniemi"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3900000, vhf_low_hz=38700000, vhf_high_hz=118700000, uhf_hz=250250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-152462.09375, 151503.710938, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield2_1'))
        self.runways.append(Runway(id=1, name='21-03', main=RunwayApproach(name='21', heading=210, beacons=[RunwayBeacon(id='airfield2_2', runway_name='21-03', runway_id=1, runway_side='21'), RunwayBeacon(id='airfield2_0', runway_name='21-03', runway_id=1, runway_side='21')]), opposite=RunwayApproach(name='03', heading=30, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-153437.71875, 151265.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-153182.484375, 151354.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S07', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-153086.90625, 151560.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-153075.078125, 151602.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-153061.28125, 151652.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-153317.03125, 151282.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-153343.46875, 151265.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-153048.734375, 151698.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-152931.765625, 151583.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S09', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-152185.390625, 151334.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-152169.875, 151346.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-152152.578125, 151357.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-152135.5, 151368.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-152118.203125, 151379.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-152100.796875, 151390.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-152083.921875, 151401.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-152067.671875, 151412.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-151928.9375, 151535.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-151908.953125, 151530.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-151887.15625, 151525.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-151866.40625, 151520.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-151844.28125, 151515.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-151822.0625, 151511.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-151800.46875, 151506.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-151779.1875, 151501.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-151757.171875, 151496.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-151679.625, 151459.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-151557.296875, 151431.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-151284.296875, 151913.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-151302.453125, 151935.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-153665.640625, 150507.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q1', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-153634.703125, 150504.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q2', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-152962.140625, 151502.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S10', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-153099.875, 151516.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-153827.546875, 150911.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Q4', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-153727.453125, 150993.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Q3', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-153122.359375, 151410.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-151191.953125, 151831.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-151138, 151805.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-151166.375, 151890.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-151111.96875, 151862.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-153250.078125, 151307.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S08', length=60.0, width=60.0, height=18.0, shelter=False))


class Kemi_Tornio(Airport):
    id = 3
    name = "Kemi Tornio"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38750000, vhf_high_hz=119400000, uhf_hz=250300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-243395.968891, 101204.631625, terrain), terrain)

        self.runways.append(Runway(id=1, name='18-36', main=RunwayApproach(name='18', heading=180, beacons=[]), opposite=RunwayApproach(name='36', heading=360, beacons=[RunwayBeacon(id='airfield3_1', runway_name='36-18', runway_id=1, runway_side='36'), RunwayBeacon(id='airfield3_0', runway_name='36-18', runway_id=1, runway_side='36')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-243722.24928481, 100891.70359519, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-243609.99166752, 100949.13069256, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-243575.53261063, 100950.33763344, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-243476.02836943, 100968.10209483, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-243387.4555893, 100970.34995285, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-243862.19937994, 100771.02116804, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D01', length=26.0, width=24.0, height=11.0, shelter=False))


class Bas_100(Airport):
    id = 4
    name = "Bas 100"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3950000, vhf_low_hz=38800000, vhf_high_hz=118250000, uhf_hz=257100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-93814.801108, 177899.306039, terrain), terrain)

        self.runways.append(Runway(id=None, name='22-4', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='4', heading=40, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-95322.140276354, 176289.25100535, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-95337.909124142, 176321.12818469, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-95310.846793899, 176141.85989576, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-95292.167041274, 176177.28856352, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-95273.277581419, 176223.81881513, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-95382.658906193, 176094.8784591, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-95349.244079159, 176098.59212581, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-91853.307181287, 179754.32999342, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-91846.893109656, 179666.45681178, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-91868.945844055, 179614.4169184, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand12', length=26.0, width=24.0, height=11.0, shelter=False))


class Kiruna(Airport):
    id = 5
    name = "Kiruna"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3975000, vhf_low_hz=38850000, vhf_high_hz=130150000, uhf_hz=250350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-20455.625, -90638.921875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield5_2'))
        self.beacons.append(AirportBeacon(id='airfield5_0'))
        self.runways.append(Runway(id=1, name='21-03', main=RunwayApproach(name='21', heading=210, beacons=[RunwayBeacon(id='airfield5_1', runway_name='21-03', runway_id=1, runway_side='21'), RunwayBeacon(id='airfield5_3', runway_name='03-21', runway_id=1, runway_side='21')]), opposite=RunwayApproach(name='03', heading=30, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-20098.654296875, -90651.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B5', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-20166.421875, -90807.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B3', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-20297.822265625, -90813.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F1', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-20283.078125, -90804.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F2', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-20268.76171875, -90794.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F3', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-20254.142578125, -90784.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F4', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-20240.12890625, -90775.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F5', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-20226.115234375, -90765.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F6', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-20237.404296875, -90748.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F7', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-20463.375, -91018.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H1', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-20114.484375, -90725.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B4', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-20419.1484375, -90913.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B1', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-20322.97265625, -90901.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B2', length=41.0, width=41.0, height=18.0, shelter=False))


class Severomorsk_3(Airport):
    id = 6
    name = "Severomorsk-3"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4000000, vhf_low_hz=38900000, vhf_high_hz=124300000, uhf_hz=250400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(148828.296875, 445899.6875, terrain), terrain)

        self.runways.append(Runway(id=1, name='35-17', main=RunwayApproach(name='35', heading=350, beacons=[]), opposite=RunwayApproach(name='17', heading=170, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(149944.75, 445795.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(148285.84375, 446432.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(148218.046875, 446411.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(147728.71875, 446163.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(147756.203125, 446158.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(147783.671875, 446154.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(147840.984375, 446129.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(147031.5, 445491.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(146912.25, 445510.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(147143.625, 445465.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(147262.65625, 445428.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(147355.375, 445467.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(147702.671875, 446167.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(146714.171875, 445278.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(146954.046875, 445226, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(147052.21875, 445258.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(147156.578125, 445291.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(146527.1875, 445336.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(148150.78125, 446391.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(147897.65625, 446122.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(147953.703125, 446112.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(147875.734375, 446400.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(147822.96875, 446403.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(147770.265625, 446406.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(147715.859375, 446409.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(146475.81548242, 445689.70594003, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(146652.90625, 445730.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(146269.03125, 445745.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(146751.625, 445756.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(147129.453125, 445855.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(147543.546875, 446424.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B50', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(147161.625, 445864.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(147193.484375, 445872.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(147224.625, 445881.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(147256.546875, 445889.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(148349.15625, 446350.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(148378.34375, 446339.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(148408.125, 446329.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(148437.046875, 446319.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(148466.21875, 446309.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(148496.171875, 446301.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(149875.71875, 446126.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(150134.484375, 446025.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(150211.859375, 446047.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(149881.59375, 445805.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(149819.265625, 445815.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(149755.359375, 445825.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(148526.296875, 446290.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(148556.859375, 446279.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(148586.984375, 446268.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(148617.3125, 446258.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(148739.609375, 446222.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(149904, 446121.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(149932.8125, 446117.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(149961.109375, 446112.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(148183.03125, 446401.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(148250, 446422.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(147900.265625, 446332.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(147938.5625, 446330.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(147977.671875, 446328.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(148015.96875, 446326.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(147743.1875, 446407.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(147796.65625, 446405.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(147849.578125, 446401.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(148835.203125, 446189.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(148930.5625, 446155.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(149565.3125, 446101.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(149464.28125, 446106.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(149727.15625, 446078.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(149827.1875, 446062.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(149930.25, 446046.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(149061.515625, 446126.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(149162.46875, 446121.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(149263.28125, 446116.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(149363.953125, 446111.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F07', length=26.0, width=24.0, height=11.0, shelter=False))


class Bodo(Airport):
    id = 7
    name = "Bodo"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4025000, vhf_low_hz=38950000, vhf_high_hz=118300000, uhf_hz=250450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-66958.882812, -348337.328125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield7_1'))
        self.beacons.append(AirportBeacon(id='airfield7_5'))
        self.runways.append(Runway(id=1, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[RunwayBeacon(id='airfield7_2', runway_name='07-25', runway_id=1, runway_side='07'), RunwayBeacon(id='airfield7_0', runway_name='07-25', runway_id=1, runway_side='07')]), opposite=RunwayApproach(name='25', heading=250, beacons=[RunwayBeacon(id='airfield7_3', runway_name='25-07', runway_id=1, runway_side='25'), RunwayBeacon(id='airfield7_4', runway_name='25-07', runway_id=1, runway_side='25')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-66660.3515625, -348583.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-66653.4296875, -348694.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-66674.0625, -348553.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-66695.0703125, -348550.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-66721.546875, -348603.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-66694.2734375, -348607.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-66715.3125, -348548.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-66734.6953125, -348546.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-66753.109375, -348544.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-67271.1015625, -348928.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-67477.546875, -350441.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-67597.625, -350495.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-66772.0859375, -349400.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-66783.171875, -348878.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-66627.5078125, -348101, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-66609.53125, -348032.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-67267.9453125, -348902.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-67264.90625, -348875.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-67329.984375, -348867.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-67333.0703125, -348894.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-67336.046875, -348921.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-67315.75, -348734.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-67318.84375, -348760.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-67321.8125, -348787.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-67256.875, -348795.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-67253.71875, -348768.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-67250.6796875, -348741.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-66607.7265625, -348479.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-66617.1484375, -348364.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-66732.75, -348155.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-67666.8515625, -350574.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-67804.375, -350472.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-67884.359375, -350571.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-67751.6953125, -350349.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-67633.9375, -350352.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-66819.578125, -349141.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-66803.171875, -349032.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-67944.6015625, -350469.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-67956.4453125, -350319.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-67925.4375, -350198.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-67405.4296875, -349966.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-67538.0390625, -349932.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-67528.234375, -350082, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-67594.78125, -349830.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-67797.2109375, -350119.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-67685.6015625, -350164.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-67774.328125, -349929.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-67668.3671875, -349954.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-67656.125, -349734.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-67399.1875, -349812.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-67459.2734375, -349735.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-66747.3671875, -348788.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-67603.84375, -349309.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-67412.8828125, -349484.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-67419, -349401.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-67388.5546875, -349319.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-67499.625, -349661.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-67482.28125, -349301.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-67655.9765625, -349559.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-67588.84375, -349652, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-67540.2421875, -349313.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-67339.0078125, -349134.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-67625.671875, -349195.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-67630.7265625, -349093.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-67544.40625, -349225.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-67732.1875, -349335.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-67764.234375, -349233.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-67840.6171875, -348929.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-67139.9765625, -347530.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-67775.2109375, -348824.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-67677.7734375, -348855.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-67655.3359375, -348760.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-67820.21875, -348757.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-67618.5546875, -348461.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-67438.65625, -348359.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-67190.9296875, -347457, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-67207.8984375, -347366.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-67106.6640625, -347275.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-67061.5546875, -347353.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-66974.8359375, -346630.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-66936.796875, -346466.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-67102.5703125, -346793.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-67174.6015625, -346865.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-67073.921875, -346880.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-67152.9375, -346973.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-67239.5625, -346929.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-67295.921875, -347008.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-67342.0859375, -347096.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-67307.75, -347198.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-67206.1875, -347045.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-67180.5546875, -347167.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-66877.4609375, -349750.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-66936.671875, -349819.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Z01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-66860.5234375, -349641.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W02', length=21.0, width=15.0, height=8.0, shelter=False))


class Severomorsk_1(Airport):
    id = 8
    name = "Severomorsk-1"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4050000, vhf_low_hz=39000000, vhf_high_hz=127800000, uhf_hz=250500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(164318.273438, 430555.578125, terrain), terrain)

        self.runways.append(Runway(id=1, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(166292.328125, 429242.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(166298.75, 429125.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(166284.34375, 429144.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(166270.9375, 429163.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(166257.015625, 429181.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(166171.703125, 429372.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(166243.203125, 429086.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(166228.625, 429104.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(166214.875, 429123.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(166201.4375, 429142.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(166187.5625, 429161.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(166227.53125, 429332.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(166100.71875, 429260.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(166139.03125, 429404.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(166105.09375, 429436.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(166072.296875, 429468.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(166006.5, 429532.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(166039.921875, 429501.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(165764.796875, 429578.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(165726.453125, 429581.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(165688.59375, 429585.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A09', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(165651.484375, 429589.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A10', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(165551.078125, 429595.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C04', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(163802.0625, 430311.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H6', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(163815.375, 430292.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H7', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(163828.546875, 430273.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H8', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(163842, 430254.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H9', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(163876.4375, 430363.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(163890.546875, 430344.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(163903.8125, 430325.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(163916.734375, 430305.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(163775.09375, 430350.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H4', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(163788.109375, 430330.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H5', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(163849.171875, 430400.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(163863.28125, 430382.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(164025.765625, 430314.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A19', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(164185.546875, 430233.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A18', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(165921.484375, 429631.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(165919.828125, 429669.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(165918.078125, 429709.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(165916.25, 429748.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(165852.875, 429746.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(165853.734375, 429706.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(165855.40625, 429666.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(165857.765625, 429628.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(166062.078125, 429320.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(166031.046875, 429349.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(165983.453125, 429361.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(165936.40625, 429445.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(165873.78125, 429458.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(164060.296875, 431391.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(164489.125, 431488.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(164571.296875, 431547.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(164669.203125, 431571.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(164631.234375, 431704.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(164728.3125, 431679.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(164772.703125, 431554.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(164388.15625, 431352.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(164541.609375, 431760.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(164446.625, 431803.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(164640.6875, 429660.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C06', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(164565.28125, 429695.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C07', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(164486.125, 429728.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C08', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(164608.109375, 430040.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C05', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(163684.734375, 430533.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H1', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(163712.53125, 430491.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H2', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(163744.5, 430444.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H3', length=42.0, width=34.0, height=14.0, shelter=False))


class Olenya(Airport):
    id = 9
    name = "Olenya"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4075000, vhf_low_hz=39050000, vhf_high_hz=131400000, uhf_hz=250550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(68386.710938, 451986.390625, terrain), terrain)

        self.runways.append(Runway(id=1, name='19-01', main=RunwayApproach(name='19', heading=190, beacons=[]), opposite=RunwayApproach(name='01', heading=10, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(66987.6875, 451434.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(67069.234375, 451445.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(67733.1875, 451562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(67656.65625, 451551.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(67582.140625, 451540.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(67507.3359375, 451530.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(67428.921875, 451519.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(67355.3828125, 451508.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(67284.25, 451499.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(67816.7890625, 451606.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(67860.0234375, 451612.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(67903.15625, 451618.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(67946.390625, 451624.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(67988.5546875, 451630.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(68031.7890625, 451636.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(68074.921875, 451642.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(68118.15625, 451648.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(68160.921875, 451654.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(68204.15625, 451660.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(68247.2890625, 451666.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(68290.5234375, 451672.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(68332.6875, 451679.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(68375.9296875, 451685.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(68419.0546875, 451691.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(68462.296875, 451697.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(68505.5, 451702.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(68548.734375, 451708.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(68590.8984375, 451715.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(68634.140625, 451721.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(68677.265625, 451727.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(68720.5078125, 451733.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(68761.296875, 451739.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(68804.4296875, 451745.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(68887.2890625, 451699.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(68943.2421875, 451707.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(68995.6953125, 451715.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(69052.046875, 451723.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(69205.9140625, 451757.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B12', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(69251.9453125, 451765.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B13', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(69300.2421875, 451771.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B15', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(69347.484375, 451777.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B16', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(69393.8203125, 451784.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B17', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(69193.921875, 451642.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(69207.2734375, 451545.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(70262.65625, 451478.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(70168.59375, 451438.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(70054.4765625, 451432.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(69946.796875, 451430.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(69851.0546875, 451428.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(69728.5625, 451461.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(69680.59375, 451550.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(69623.0078125, 451656.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(69578.421875, 451738.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(69292.5234375, 451220.53014259, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(69284.445589352, 451277.43528518, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(69276.237163735, 451334.02484197, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(69268.31026497, 451390.6280858, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(69260.604628087, 451447.22017468, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(69699.953125, 450826.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D12', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(69787.0546875, 450728.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D13', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(69631.4296875, 450904.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D11', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(69520.4140625, 450958.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D10', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(69417.8046875, 450965.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(69316.8828125, 450972.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(69662.9140625, 451842.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B18', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(69793.3984375, 451861.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B19', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(69870.4921875, 451871.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand01', length=60.0, width=52.0, height=18.0, shelter=False))


class Monchegorsk(Airport):
    id = 10
    name = "Monchegorsk"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3775000, vhf_low_hz=38450000, vhf_high_hz=118100000, uhf_hz=250050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(46867.561851, 437312.674304, terrain), terrain)

        self.runways.append(Runway(id=1, name='01-19', main=RunwayApproach(name='01', heading=10, beacons=[]), opposite=RunwayApproach(name='19', heading=190, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(46124.52734375, 436935.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(46142.1015625, 436937.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(46106.88671875, 436934.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(46177.171875, 436939.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(46194.73828125, 436941.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(46159.42578125, 436938.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(46212.3125, 436942.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(46229.65625, 436943.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(46264.7109375, 436945.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(46247.07421875, 436944.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(45864.591392535, 437242.44888839, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J01', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(46736.31640625, 436790.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(46765.0703125, 436807, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(46707.96484375, 436774.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(46794.51953125, 436824.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(46823.29296875, 436840.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(46857.22265625, 436858.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(47731.046875, 437289.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(47725.20703125, 437308.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(47718.65234375, 437329.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(47712.453125, 437350.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(47706.06640625, 437369.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(47700.15234375, 437390.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(47693.25390625, 437412.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(47687.1328125, 437432.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(47829.71875, 437203.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(47793.59375, 437279.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(48064.234375, 437398.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(48050.82421875, 437382.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(46053.23046875, 436738.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(46024.15625, 436738.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(46911.05078125, 436996.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(46992.6015625, 437044.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(47628.09765625, 437281.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(46914.52734375, 436902.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(46944.18359375, 436919.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(46972.08984375, 436935.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(47002.4921875, 436953.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(47030.703125, 436969.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(47060.3046875, 436986.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(47088.01953125, 437004.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(47116.1953125, 437020.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(47145.0078125, 437037.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(46886.28125, 436885.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(45849.109375, 436660.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(45799.615872456, 436749.71764212, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(46131.99609375, 437271.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J02', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(45779.300244836, 436819.83314653, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(45132.1015625, 436312.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(45696.217604629, 436873.66622598, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(45704.534276165, 436845.67919332, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(46451.4375, 436793.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(45685.40625, 437180.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(47317.82421875, 437213.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(47498.2109375, 437104.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(47411.765625, 437233.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(47491.046875, 437256.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(47181.8671875, 437166.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(47251.84765625, 437188.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(47747.87890625, 437211.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(47557.0234375, 437133.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(47933.1796875, 437185.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(47972.66015625, 437224.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(47998.0546875, 437284.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(48042.68359375, 437318.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(47960.27734375, 437397.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(47241.19140625, 437025.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(47302.22265625, 437040.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(47366.73828125, 437062.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(45548.55859375, 437202.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(45522.1796875, 437261.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(45624.0234375, 437301.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(45653.640625, 437242.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(46562.69921875, 436896.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(46486.3671875, 436874.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(46256.0078125, 436760.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(46365.62890625, 436775.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(46161.69921875, 436760.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(46099.4453125, 436755.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(45350.19921875, 436406.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(45402.11328125, 436431, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(45320.21484375, 436524.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(45411.3984375, 436578.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(45460.7734375, 436652.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(45519.41796875, 436683.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(45591.078125, 436681.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(46258.95703125, 436664.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(46162.6875, 436653.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(45994.78125, 436799.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(45916.9453125, 436800.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(45844.51953125, 436756.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(45983.125, 436644.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(45931.42578125, 436640.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(45792.858298527, 436773.20814653, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(45786.143994836, 436796.33176492, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(45705.42578125, 436711.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='I01', length=26.0, width=24.0, height=11.0, shelter=False))


class Murmansk_International(Airport):
    id = 12
    name = "Murmansk International"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=127300000, uhf_hz=250150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(131730.496094, 409479, terrain), terrain)

        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[RunwayBeacon(id='airfield12_1', runway_name='13-31', runway_id=1, runway_side='13'), RunwayBeacon(id='airfield12_3', runway_name='13-31', runway_id=1, runway_side='13')]), opposite=RunwayApproach(name='31', heading=310, beacons=[RunwayBeacon(id='airfield12_2', runway_name='31-13', runway_id=1, runway_side='31'), RunwayBeacon(id='airfield12_0', runway_name='31-13', runway_id=1, runway_side='31')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(131927.1875, 409564.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A9', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(131957.546875, 409593.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A7', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(131987.890625, 409622.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A5', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(132018.484375, 409652.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A3', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(132048.953125, 409681.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A1', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(132146.90625, 409576.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A2', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(132112.15625, 409543.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A4', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(132074.78125, 409507.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A6', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(132036.453125, 409467.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A8', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(132377.46875, 409181.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B5', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(132422.46875, 409229.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B6', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(132388.234375, 409265.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B4', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(132343.03125, 409309.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B2', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(132307.265625, 409251.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B1', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(132260.28125, 409241.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PP', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(132341.640625, 409217.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B3', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(132233.46875, 409303.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C1', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(132251.890625, 409323.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C2', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(132270.40625, 409342.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C3', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(132289.078125, 409361.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C4', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(132307.625, 409380.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C5', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(132325.734375, 409399.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C6', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(132344.171875, 409417.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C7', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(132189.875, 409346.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(132209, 409365.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(132227.515625, 409384.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(132245.953125, 409404.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(131094.046875, 410512.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(131225.296875, 410377.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=61.0, width=61.0, height=20.0, shelter=False))


class Kalixfors(Airport):
    id = 13
    name = "Kalixfors"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=118200000, uhf_hz=301100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-26773.458984, -94330.128906, terrain), terrain)

        self.runways.append(Runway(id=1, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-26574.47265625, -93873.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-26558.90234375, -93920.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-26543.853515625, -93964.734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-26528.845703125, -94010.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-26513.2734375, -94057.2734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-26498.265625, -94103.1640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-26483.26953125, -94147.1796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-26468.259765625, -94193.0703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-26452.689453125, -94239.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-26986.921875, -93969.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-26954.1484375, -93922.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-26923.169921875, -93876.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-26891.169921875, -93831.2734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-27116.623046875, -94154.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-27083.849609375, -94107.515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-27052.87109375, -94061.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-27020.87109375, -94016.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P04', length=42.0, width=34.0, height=14.0, shelter=False))


ALL_AIRPORTS: List[Type[Airport]] = [
    Banak,
    Rovaniemi,
    Kemi_Tornio,
    Bas_100,
    Kiruna,
    Severomorsk_3,
    Bodo,
    Severomorsk_1,
    Olenya,
    Monchegorsk,
    Murmansk_International,
    Kalixfors,
]

