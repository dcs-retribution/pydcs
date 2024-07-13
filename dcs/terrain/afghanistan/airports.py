# flake8: noqa
from typing import List, Type

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


class Herat(Airport):
    id = 1
    name = "Herat"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3750000, vhf_low_hz=38400000, vhf_high_hz=123350000, uhf_hz=240300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(25820.932617, -371274.640625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield1_1'))
        self.beacons.append(AirportBeacon(id='airfield1_2'))
        self.beacons.append(AirportBeacon(id='airfield1_0'))
        self.runways.append(Runway(id=1, name='18-36', main=RunwayApproach(name='18', heading=180, beacons=[]), opposite=RunwayApproach(name='36', heading=360, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(24805.064453125, -371586.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(24899.806640625, -371596.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='27', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(25017.349609375, -371594.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(25127.365234375, -371525.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(25260.130859375, -371640.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(25142.24609375, -371651.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(24802.30859375, -371566.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(26263.19921875, -371445.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(26281.606004408, -371509.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(25115.08984375, -371127.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(25085.728515625, -371131.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(25134.6171875, -371592, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(24892.541015625, -371545.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='28', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(25251.720703125, -371571.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(26242.841796875, -371374.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(26317.997436171, -371504.255158, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(26765.751953125, -371333, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(24849.181640625, -371580.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(24852.064453125, -371599.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(24846.357421875, -371560.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(24682.287109375, -371605.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(26759.4765625, -371297.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(25012.798828125, -371537.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(26913.404296875, -371295.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(25270.53125, -371226.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(24808.091796875, -371606.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(26866.115234375, -371334.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(25016.314453125, -371139.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(24744.33984375, -371592.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(25056.677734375, -371133.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(26856.20703125, -371269.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(25143.75390625, -371123.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(25246.85546875, -371535.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(26269.365234375, -371493.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(26414.80859375, -371388.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(25256.435546875, -371609.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))


class Farah(Airport):
    id = 2
    name = "Farah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3975000, vhf_low_hz=38850000, vhf_high_hz=118100000, uhf_hz=250300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-178644.117188, -378451.53125, terrain), terrain)

        self.runways.append(Runway(id=1, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-178336.1875, -378807.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-178305.703125, -378827.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-178370.796875, -378793.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))


class Shindand(Airport):
    id = 3
    name = "Shindand"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3800000, vhf_low_hz=38500000, vhf_high_hz=134750000, uhf_hz=265650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-64594.521484, -368871.46875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield3_0'))
        self.runways.append(Runway(id=1, name='36-18', main=RunwayApproach(name='36', heading=360, beacons=[]), opposite=RunwayApproach(name='18', heading=180, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-63210.84765625, -369221.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-63284.1953125, -367989.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-63261.75390625, -369211.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-66026.3359375, -369241.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-65564.4140625, -368037.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-63837.5, -369160.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-63226.5703125, -368007.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-65603.640625, -369302.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-65944.6328125, -369238.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-63472.3359375, -369172.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-63470.859375, -369219, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-65680.359375, -368121.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-65682.265625, -368042.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-65557.8359375, -368158.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-63140.3828125, -369186.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-63618.30859375, -369177.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-64017.796875, -369167.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-63280.5234375, -368070.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-63224.19140625, -368048.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-65920.5703125, -369237, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-63714.94140625, -369196.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-63835.83203125, -369201.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-65581.0703125, -369301.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-63541.65625, -369174.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-63777.2890625, -369158.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-63284.34765625, -368030.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-65646.109375, -368074.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-65560.5234375, -368115.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-63539.51953125, -369221.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-63897.05078125, -369203.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-65682.2421875, -368075.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-65647.8984375, -368041.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-65642.5859375, -368162.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-65094.18359375, -369296.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-63716.578125, -369156.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-65678.40625, -368164.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-63222.44921875, -368089.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-65130.859375, -369296.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-63474.13671875, -369195.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-63957.05078125, -369165.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-63228.557013427, -367966.2591124, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-65627.0546875, -369303.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-63614.8125, -369200.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-63538.171875, -369198.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-63955.37890625, -369205.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-65969.8203125, -369239.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-65999.734375, -369240.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-64016.59765625, -369207.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-63776.0546875, -369199.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-63898.25, -369162.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-65644.2578125, -368119.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-65561.875, -368070.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=11.0, shelter=False))


class Maymana_Zahiraddin_Faryabi(Airport):
    id = 4
    name = "Maymana Zahiraddin Faryabi"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=38650000, vhf_high_hz=118150000, uhf_hz=250150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(218034.484375, -141298.265625, terrain), terrain)

        self.runways.append(Runway(id=None, name='32-14', main=RunwayApproach(name='32', heading=320, beacons=[]), opposite=RunwayApproach(name='14', heading=140, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(217636.640625, -140812.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(218347.109375, -141370.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(218372.03125, -141390.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(217655.375, -140827.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(218289.21875, -141388.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(218393.515625, -141458.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(218292.265625, -141328.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(218329.453125, -141417.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(218304.15625, -141400.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(218188.65625, -141303.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(218210.296875, -141272.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(218263.890625, -141368.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(218321.265625, -141350.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(218365.96875, -141448.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(218409.75, -141418.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(217678.03125, -140847.671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(218352, -141437.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))


class Chaghcharan(Airport):
    id = 5
    name = "Chaghcharan"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=118000000, uhf_hz=250050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(63224.144531, -91680.816406, terrain), terrain)

        self.runways.append(Runway(id=None, name='25-7', main=RunwayApproach(name='25', heading=250, beacons=[]), opposite=RunwayApproach(name='7', heading=70, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(63186.81640625, -92088.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(63161.65625, -92142.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(63178.22265625, -92117.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=18.0, height=8.0, shelter=False))


class Qala_i_Naw(Airport):
    id = 6
    name = "Qala i Naw"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4000000, vhf_low_hz=38900000, vhf_high_hz=118350000, uhf_hz=250350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(111818.191406, -289403.359375, terrain), terrain)

        self.runways.append(Runway(id=1, name='22-04', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='04', heading=40, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(111898.5078125, -289440.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(111918.8046875, -289462.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(111867.16098792, -289435.3033876, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(111955.0546875, -289392.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(111898.0791032, -289409.89162711, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(111872.328125, -289279.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(111943.52906755, -289370.40823031, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(111882.42055118, -289422.34565857, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(111958.63246688, -289357.34940396, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(111887.953125, -289264.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(111851.87000253, -289447.93757174, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(111928.18348072, -289383.03323031, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(111973.15625, -289414.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(111857.015625, -289293.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(111904.765625, -289251.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=18.0, height=8.0, shelter=False))


class Kandahar(Airport):
    id = 7
    name = "Kandahar"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4025000, vhf_low_hz=38950000, vhf_high_hz=125500000, uhf_hz=360200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-270486.3125, -29690.017578, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield7_1'))
        self.beacons.append(AirportBeacon(id='airfield7_0'))
        self.runways.append(Runway(id=1, name='23-05', main=RunwayApproach(name='23', heading=230, beacons=[]), opposite=RunwayApproach(name='05', heading=50, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-272034.96875, -31256.265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DOS04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-269990.71875, -29587.03515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-271448.5, -30367.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M10', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-271932.65625, -31077.80078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DOS11', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-269814.96875, -29871.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y14', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-269842.9375, -29854.57421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y15', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-272017.1875, -31236.662109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DOS05', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-272302.3125, -31442.486328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='O05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-270161.65625, -29780.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-269128.6875, -28668.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T20', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-270483.90625, -29132.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='I06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-270177.21875, -29802.51171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-272339.78125, -31604.32421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Q04-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-272246.8125, -31483.994140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='O03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-271281.6875, -30217.326171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L06-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-270023.28125, -28432.802734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-269356.0625, -28965.607421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-269703.25, -29411.69921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-269373.09375, -29116.048828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W14', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-269646.65625, -27970.994140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-270046.1875, -29862.123046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-271265.5625, -30107.853515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L15-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-269872.6875, -29460.03515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-270497.9375, -29242.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='I01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-272230.5, -31402.64453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='O07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-269558.96875, -29139.44140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W18', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-269286.0625, -28892.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='V05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-270149.9375, -28626.044921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-269415.75, -28920.337890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-269866.3125, -28141.822265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='AAF05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-272314.96875, -31623.98828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Q03-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-272218.71875, -31504.185546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='O02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-269174.1875, -28635.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-271787.59375, -30856.880859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N22', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-272203.1875, -31423.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='O08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-268951.28125, -28706.619140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T11', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-271718.90625, -30907.08203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N25', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-269019.5, -28749.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T15', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-271821.5625, -30936.556640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-271047.875, -31144.521484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DAC01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-269365.1875, -29310.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-270351.71875, -28948.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-269164.1875, -28819.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-270091.1875, -29924.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-270272.71875, -28784.521484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H15', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-269215.8125, -28778.05859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U08', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-270185.5, -28633.501953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-269658.21875, -27988.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-271788.46875, -30961.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-270104.15625, -29788.318359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z11', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-270027.625, -28542.384765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-269981.09375, -29846.298828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-269873.34375, -29572.837890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X19', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-270224.96875, -28768.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H16', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-270099.5, -28598.478515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-271838.71875, -30923.044921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N13', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-269014.625, -28661.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T08', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-269040.5625, -28639.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-271764.03125, -30806.896484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M02', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-270205.59375, -29842.884765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-271300.25, -30203.89453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L07-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-269084.40625, -28608.55078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-269987.125, -28383.595703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-270010.40625, -29887.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-272003.8125, -31213.4609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DOS06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-269778.1875, -28254.755859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF04', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-271245.9375, -30243.59765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L01-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-269725.5, -29395.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-269994.09375, -28455.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-270061.1875, -29882.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-272415.65625, -31545.294921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Q07-H', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-269760.75, -29456.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-269039.34375, -28733.853515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T16', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-271266.875, -30196.79296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L05-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-271852.15625, -30883.251953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-271687.1875, -30852.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-270818.46875, -29496.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-269821.90625, -29705.240234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-270333.46875, -28894.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-270394.34375, -29006.49609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-269597.21875, -27901.685546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-269242.9375, -28759.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U09', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-269793.0625, -29518.068359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-269767.09375, -29537.08984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-269969.6875, -28328.806640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-271921.65625, -31002.833984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-269694.65625, -28084.962890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-270150.15625, -29851.333984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z08', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-271534.4375, -30487.943359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M07', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-269689.4375, -29817.646484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y10', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-270076.1875, -29903.830078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-270210.21875, -29986.298828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-269680.21875, -28064.72265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-269738.625, -29260.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='UAE10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-272146.46875, -31463.21484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='O10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-269764.25, -29744.10546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y08', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-271302.5625, -30304.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M11', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-269651.5, -28025.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF14', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-272263.78125, -31663.931640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Q01-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-271618.09375, -30601.189453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M06', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-269294.65625, -29044.833984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-269792.59375, -29347.55859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-269189.09375, -28797.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-269762.21875, -29243.583984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='UAE11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-269734.875, -29476.025390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-269649.28125, -29241.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='UAE03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-271180.65625, -29998.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-271555.21875, -30652.595703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M05', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-270165.09375, -29872.169921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-270536.375, -29204.12109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='I03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-271216.28125, -30203.4765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L03-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-271989.1875, -31192.884765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DOS07', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-270040.3125, -29711.35546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y21', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-270227.25, -28841.923828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-270008.59375, -28443.72265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-271837.9375, -31064.63671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-269312.59375, -29033.322265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-269698.3125, -29206.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='UAE01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-271385.3125, -30415.552734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M09', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-269393.96875, -28814.34765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='V01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(-271960.96875, -31156.296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DOS09', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(-271803.96875, -30949.044921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-269964.625, -28476.544921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-270424.0625, -30186.48828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-271335.96875, -30177.623046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L12-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(-270362.25, -29053.255859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(-270277.5, -28886.287109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(-269708.0625, -28058.021484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(-270135.5, -28667.017578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(-269801.9375, -29425.30078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(-269633.40625, -27954.44921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(-269870.40625, -29834.294921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y16', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(-269625.28125, -29259.263671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='UAE04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(-269168, -28740.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(-269058.15625, -28720.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T17', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(-269445.21875, -29330.685546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(-272366.25, -31585.892578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Q05-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(-269063.5, -28623.794921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(-269690.25, -29296.40234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='UAE08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(-269710, -29846.68359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y11', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(-270191.125, -29821.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(-270467.0625, -29109.861328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='I07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(-270109.21875, -28684.568359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G08', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(-270308.25, -28822.876953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(-271270.5625, -30163.771484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L09-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(-270552.9375, -29226.869140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='I02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(-270444.5, -29168.740234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='I08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(-271190.84375, -30162.62109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L13-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(-269730.0625, -29872.994140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y12', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(-272391.0625, -31565.974609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Q06-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(-271865.6875, -31043.861328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(-269272.28125, -29059.23046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(-272289.46875, -31644.330078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Q02-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(-269604.59375, -27960.69921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(-268974.90625, -28689.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T10', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(-270339.84375, -30115.169921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=157, position=mapping.Point(-269608.09375, -27920.205078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=158, position=mapping.Point(-271252.125, -30176.96484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L04-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=159, position=mapping.Point(-271829.3125, -30899.365234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=160, position=mapping.Point(-270302.875, -28973.37109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=161, position=mapping.Point(-269296.9375, -28720.658203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=162, position=mapping.Point(-269835.375, -28336.755859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF02', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=163, position=mapping.Point(-271862.25, -30957.201171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=164, position=mapping.Point(-269106.34375, -28682.06640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T19', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=165, position=mapping.Point(-269634.78125, -28002.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=166, position=mapping.Point(-269822, -29497.044921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=167, position=mapping.Point(-269862, -29380.845703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=168, position=mapping.Point(-271321.1875, -30157.08984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L11-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=169, position=mapping.Point(-269991.21875, -28492.18359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=170, position=mapping.Point(-271620.4375, -30745.88671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M04', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=171, position=mapping.Point(-270334.875, -28925.650390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=172, position=mapping.Point(-270467.375, -29048.951171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=173, position=mapping.Point(-269925.4375, -28361.408203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN18', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=174, position=mapping.Point(-270272.8125, -30164.400390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=175, position=mapping.Point(-269720.9375, -28075.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=176, position=mapping.Point(-271241.59375, -30126.26171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L14-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=177, position=mapping.Point(-270145.71875, -29757.763671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=178, position=mapping.Point(-270014.03125, -29730.07421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y20', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=179, position=mapping.Point(-270031.25, -29841.302734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=180, position=mapping.Point(-269599.375, -29277.16796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='UAE05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=181, position=mapping.Point(-270368.5625, -28971.41015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=182, position=mapping.Point(-270500.75, -29155.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='I05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=183, position=mapping.Point(-270696.8125, -29412.32421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=184, position=mapping.Point(-269665.8125, -28044.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=185, position=mapping.Point(-269898.84375, -28278.021484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='AAF01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=186, position=mapping.Point(-270302.96875, -28867.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=187, position=mapping.Point(-272047.5625, -31279.4609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DOS03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=188, position=mapping.Point(-269738.1875, -29764.451171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y09', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=189, position=mapping.Point(-270146.1875, -28734.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=190, position=mapping.Point(-271231.1875, -30223.6015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L02-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=191, position=mapping.Point(-271306.4375, -30137.259765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L10-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=192, position=mapping.Point(-269749.8125, -29900.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y13', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=193, position=mapping.Point(-269792.96875, -29722.9765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=194, position=mapping.Point(-271080.9375, -29892.802734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K06', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=195, position=mapping.Point(-272110.46875, -31325.052734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DOS01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=196, position=mapping.Point(-269250.875, -28687.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=198, position=mapping.Point(-269957.21875, -29770.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y18', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=199, position=mapping.Point(-269228.75, -29090.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W08', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=200, position=mapping.Point(-269590.5625, -27941.287109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF23', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=201, position=mapping.Point(-270162.90625, -30020.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=202, position=mapping.Point(-270196.40625, -28698.888671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=203, position=mapping.Point(-270757, -29412.44921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=204, position=mapping.Point(-270046.75, -28568.888671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=205, position=mapping.Point(-269911.96875, -29544.783203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X18', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=206, position=mapping.Point(-271468.96875, -30539.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M08', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=207, position=mapping.Point(-271975.75, -31175.228515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DOS08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=208, position=mapping.Point(-269940.25, -28350.53515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=209, position=mapping.Point(-270410.625, -29030.76171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=210, position=mapping.Point(-269151.6875, -28652.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T21', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=211, position=mapping.Point(-270202.25, -28784.23828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H17', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=212, position=mapping.Point(-271683.84375, -30696.587890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M03', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=213, position=mapping.Point(-269576.375, -27921.845703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=214, position=mapping.Point(-269333.9375, -29016.794921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=215, position=mapping.Point(-269197.03125, -28724.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=216, position=mapping.Point(-272274.09375, -31462.712890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='O04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=217, position=mapping.Point(-269712.28125, -29280.50390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='UAE09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=218, position=mapping.Point(-272067.71875, -31301.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DOS02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=219, position=mapping.Point(-269840.46875, -29396.57421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=220, position=mapping.Point(-269933.96875, -29628.240234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=221, position=mapping.Point(-269222.6875, -28701.978515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=222, position=mapping.Point(-269979.34375, -28465.82421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=223, position=mapping.Point(-269802.4375, -28067.63671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='AAF06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=224, position=mapping.Point(-270220.03125, -28680.474609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=225, position=mapping.Point(-269085.84375, -28701.869140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T18', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=226, position=mapping.Point(-269845.125, -29480.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=227, position=mapping.Point(-271945.84375, -31136.826171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='DOS10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=228, position=mapping.Point(-271893.71875, -31023.326171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=229, position=mapping.Point(-269480.15625, -29191.150390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W19', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=230, position=mapping.Point(-271767.5, -30871.802734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N23', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=231, position=mapping.Point(-268974.65625, -28782.55859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T13', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=232, position=mapping.Point(-271143.875, -30024.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=233, position=mapping.Point(-269211.90625, -28543.15234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=234, position=mapping.Point(-272191.25, -31524.865234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='O01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=235, position=mapping.Point(-269269.28125, -28739.275390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U10', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=236, position=mapping.Point(-269985.96875, -29748.337890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y19', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=237, position=mapping.Point(-270136.5, -29832.505859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z09', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=238, position=mapping.Point(-270375.65625, -30222.087890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=239, position=mapping.Point(-271778.1875, -30936.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=240, position=mapping.Point(-270718.25, -29441.65234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=241, position=mapping.Point(-271809.4375, -30838.287109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=242, position=mapping.Point(-271803.40625, -30917.70703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=243, position=mapping.Point(-270176.625, -28803.70703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H18', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=244, position=mapping.Point(-269755.3125, -29374.568359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=245, position=mapping.Point(-269780.59375, -29440.794921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=246, position=mapping.Point(-269312.75, -28872.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='V04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=247, position=mapping.Point(-270130.90625, -29737.283203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=248, position=mapping.Point(-268996.34375, -28675.119140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T09', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=249, position=mapping.Point(-269905.40625, -28376.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN19', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=250, position=mapping.Point(-269622.375, -27936.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=251, position=mapping.Point(-271855.6875, -30910.966796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N12', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=252, position=mapping.Point(-270252.46875, -28823.115234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=253, position=mapping.Point(-269806.90625, -28295.63671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF03', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=254, position=mapping.Point(-269903.375, -29437.138671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=255, position=mapping.Point(-271367.5625, -30255.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M12', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=256, position=mapping.Point(-269957.9375, -28405.544921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN13', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=257, position=mapping.Point(-269128.40625, -28572.82421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=258, position=mapping.Point(-269196.75, -28560.423828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=259, position=mapping.Point(-269641.125, -29333.01953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='UAE06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=260, position=mapping.Point(-271119.03125, -29923.771484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=261, position=mapping.Point(-269943.125, -28416.294921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=262, position=mapping.Point(-270009.375, -28517.60546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=263, position=mapping.Point(-270057.25, -28598.935546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=264, position=mapping.Point(-268996.5625, -28768.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T14', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=265, position=mapping.Point(-269671.15625, -28005.86328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=266, position=mapping.Point(-270120.3125, -29810.44921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z10', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=267, position=mapping.Point(-269972.40625, -28394.443359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN12', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=268, position=mapping.Point(-270089.4375, -29767.73828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z12', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=269, position=mapping.Point(-270521.5, -29184.44140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='I04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=270, position=mapping.Point(-270016.5, -29821.06640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=271, position=mapping.Point(-269394.8125, -29100.591796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W15', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=272, position=mapping.Point(-269683.375, -28023.28515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=273, position=mapping.Point(-269367.09375, -28834.330078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='V02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=274, position=mapping.Point(-271285.46875, -30183.896484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L08-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=275, position=mapping.Point(-272257.9375, -31381.947265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='O06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=276, position=mapping.Point(-269819.8125, -29328.619140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=277, position=mapping.Point(-269666.84375, -29314.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='UAE07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=278, position=mapping.Point(-270025.78125, -29908.490234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=279, position=mapping.Point(-269696.625, -28040.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=280, position=mapping.Point(-270327.25, -30257.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=281, position=mapping.Point(-269443.25, -29084.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W16', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=282, position=mapping.Point(-270040.59375, -29929.384765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=283, position=mapping.Point(-269108.65625, -28593.900390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=284, position=mapping.Point(-269619.03125, -27980.880859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='AAF19', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=285, position=mapping.Point(-269671.1875, -29225.255859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='UAE02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=286, position=mapping.Point(-271830.0625, -30983.197265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=287, position=mapping.Point(-270055.375, -29950.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=288, position=mapping.Point(-269339.9375, -28853.36328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='V03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=289, position=mapping.Point(-269907.34375, -29647.861328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=290, position=mapping.Point(-269143.0625, -28764.705078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=291, position=mapping.Point(-270160.59375, -28649.82421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=292, position=mapping.Point(-271894.625, -30930.470703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N10', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=293, position=mapping.Point(-269878.65625, -29668.185546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=294, position=mapping.Point(-270257.90625, -29951.501953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=295, position=mapping.Point(-272175.09375, -31443.728515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='O09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=296, position=mapping.Point(-270734.28125, -29381.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=297, position=mapping.Point(-270780.875, -29526.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=298, position=mapping.Point(-269316.96875, -29156.873046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W11', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=299, position=mapping.Point(-271088.125, -29947.416015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=300, position=mapping.Point(-268929.78125, -28721.591796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T12', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=301, position=mapping.Point(-271846.09375, -30970.19921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=302, position=mapping.Point(-271878.53125, -30943.658203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=303, position=mapping.Point(-270171.84375, -28716.849609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=304, position=mapping.Point(-271813.5, -30996.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=305, position=mapping.Point(-270066.53125, -29693.255859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=306, position=mapping.Point(-269962.875, -29606.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=307, position=mapping.Point(-269334.125, -29144.345703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W12', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=308, position=mapping.Point(-271872.0625, -30898.99609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=309, position=mapping.Point(-271198.125, -30033.587890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=310, position=mapping.Point(-270002, -28372.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN10', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=311, position=mapping.Point(-269954.9375, -28339.697265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='PAN16', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=312, position=mapping.Point(-269254.03125, -29070.916015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=313, position=mapping.Point(-269995.4375, -29866.978515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=314, position=mapping.Point(-269513.3125, -29034.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W17', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=315, position=mapping.Point(-269898.53125, -29815.099609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Y17', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=316, position=mapping.Point(-271744.5, -30888.529296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N24', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=317, position=mapping.Point(-269355.90625, -29128.751953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W13', length=20.0, width=18.0, height=8.0, shelter=False))


class Bost(Airport):
    id = 8
    name = "Bost"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4050000, vhf_low_hz=39000000, vhf_high_hz=131250000, uhf_hz=243000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-267202.0625, -170619.5625, terrain), terrain)

        self.runways.append(Runway(id=1, name='01-19', main=RunwayApproach(name='01', heading=10, beacons=[]), opposite=RunwayApproach(name='19', heading=190, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-267082.59375, -170712.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-267080.28125, -170737.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-267085.15625, -170689.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-267152.8125, -170723.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=36.0, width=36.0, height=15.0, shelter=False))


class Tarinkot(Airport):
    id = 9
    name = "Tarinkot"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4075000, vhf_low_hz=39050000, vhf_high_hz=128000000, uhf_hz=250400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-148524.9375, -31352.183594, terrain), terrain)

        self.runways.append(Runway(id=1, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-148400.796875, -31236.837890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-148497.953125, -31072.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-149089.3125, -30945.94921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C17-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-149049.984375, -31040.22265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C07-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-149069.171875, -30930.6640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C18-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-148932.15625, -31031.935546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C02-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-148973.421875, -30444.892578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-149109.09375, -30961.1171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C16-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-148992.25, -31077.208984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C05-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-148971.625, -30980.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C10-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-148994.640625, -30459.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-149078.484375, -31001.89453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C15-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-148451.765625, -31156.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-148986.78125, -30368.05859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-149038.8125, -30971.669921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C13-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-149049.265625, -30915.55859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C19-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-148952.328125, -31046.8984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C03-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-148366, -31289.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-149011.015625, -30886.62109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C21-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-148912.671875, -31016.638671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C01-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-148972.328125, -31061.921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C04-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-148434.046875, -31182.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-148998.640625, -30941.681640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C11-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-148348.5, -31316.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-148383.234375, -31263.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-149029.375, -30900.166015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C20-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-149018.8125, -30956.64453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C12-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-148469.265625, -31129.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-148997.546875, -30999.9453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C09-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-149058.734375, -30986.95703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C14-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-149023.34375, -31019.595703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C08-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-148417.328125, -31209.767578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-149011.984375, -31092.1484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C06-H', length=20.0, width=17.0, height=8.0, shelter=False))


class Camp_Bastion(Airport):
    id = 10
    name = "Camp Bastion"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3900000, vhf_low_hz=38700000, vhf_high_hz=123300000, uhf_hz=250100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-235177.570313, -184376.585938, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield10_1'))
        self.beacons.append(AirportBeacon(id='airfield10_0'))
        self.runways.append(Runway(id=1, name='01-19', main=RunwayApproach(name='01', heading=10, beacons=[]), opposite=RunwayApproach(name='19', heading=190, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-235660.28125, -184155.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-235577.375, -184099.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='J10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-234179.203125, -183706.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L47', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-235135.71875, -184053.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-236297.0625, -185178.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E08', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-236018.03125, -184286.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-235386.75, -184108.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-236303.5625, -185146.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E09', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-234076.15625, -183932.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-234460.109375, -183924.171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K10-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-234008.390625, -183747.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-233880.234375, -183725.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-234209.1875, -183897.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-234135.453125, -183884.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-236207.875, -185226.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-235391.78125, -184066.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-233944.421875, -183734.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-236580.203125, -184269.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-235755.484375, -184130.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-234427.90625, -183942.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K18-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-236489.40625, -184214.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='G05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-235295.546875, -185026.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-234125.25, -183940.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-236897.140625, -184855.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='SA02', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-235542.328125, -185213.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C10', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-233963.015625, -183853.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-233987.75, -183858.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-234432.25, -183919.265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K19-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-234522.109375, -184005.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K02-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-234360.6875, -183907, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K24-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-233803.21875, -183708.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='L37', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-236218.84375, -185165.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-236882.25, -184940.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='SA01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-235667.8125, -184114.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-236292.25, -185208.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-235226.703125, -184037.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-235938.296875, -184156.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-235467.390625, -185200.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-235322.484375, -185144.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-235653.875, -184197.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-234051.296875, -183689.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L43', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-235854.953125, -185151.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-236581, -184230.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='G04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-236475.34375, -184292.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-234415.671875, -184010.734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K15-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-235852.40625, -184270.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-234345.90625, -183974.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K27-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-235277.875, -185138.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-233359.734375, -184325.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-234110.96875, -183879.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-236225.28125, -185132.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-234136.734375, -183768.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-234530.046875, -183960.015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K04-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-235739.25, -183965.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J26', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-235222.3125, -183875.390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J30', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-234370.59375, -183861.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K22-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-234436.140625, -183896.578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K20-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-234464.546875, -183901.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K09-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-234104.328125, -183763.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-234160.125, -183887.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-235863.484375, -184210, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-234243.203125, -183718.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L49', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-234147.453125, -183706.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L46', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-235920.4375, -184258.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-234061.703125, -183870.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-235563.21875, -184181.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='J08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-234184.5, -183893.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-236468.3125, -184333.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-235368.234375, -185150.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-236572.78125, -184310.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-236564.390625, -184350.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-234199.1875, -183955.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-233374.28125, -184238.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='NA02', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-235210.953125, -184119.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-234456.3125, -183947.140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K11-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-233987.1875, -183679.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-235122.96875, -184121.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-235674.640625, -184075.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-235571.6875, -184139.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-234361.96875, -183883.515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K23-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-235129.4375, -184087.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-234086.015625, -183876.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-234072.171875, -183758.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-234027.25, -183923.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-234452.125, -183969.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K12-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-235695.71875, -185124.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-235493.203125, -185050.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C09', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-235297.78125, -184134.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-234084.3125, -183693.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L44', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-235378.90625, -184148.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-233977.734375, -183914.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-235482.046875, -185114.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-234531.109375, -183936.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K05-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-234168.375, -183775.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-235584.328125, -184059, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='J11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-235304.453125, -184093.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-235218.734375, -184078.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-234523.25, -183982.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K03-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-235741.484375, -184213.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-233912, -183730.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-234200.140625, -183781.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-235561.15625, -183935.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J28', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-234149.8125, -183946.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-233976.6875, -183739.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-235908.296875, -184021.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-234100.546875, -183938.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-234232.375, -183786.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-235311.296875, -184052.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-235649.9375, -183949.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J27', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-235141.796875, -184019.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-235926.421875, -184224.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-234019.25, -183684.921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L42', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-234443.78125, -184015.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K14-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-235565.59375, -185063.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C12', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-233923.265625, -183666.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L39', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-236202.53125, -185258.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-236019.96875, -185181, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-234174.640625, -183949.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-234036.9375, -183867, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(-234012.390625, -183861.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(-234352.5, -183952.296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K26-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-234539.1875, -183891.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K07-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-234624.859375, -184917.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-234117.046875, -183698.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L45', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(-234732.625, -184940.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(-234467.734375, -183878.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K08-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(-234448.015625, -183992.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K13-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(-233955.140625, -183673.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L40', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(-234423.859375, -183964.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K17-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(-235385.90625, -185039.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C06', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(-234354.125, -183929.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K25-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(-233928.234375, -183906.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(-235747.90625, -184170.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(-233952.9375, -183912.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(-235307.1875, -183891.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J29', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(-234051.46875, -183929.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(-234515.765625, -184897.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(-234210.28125, -183712.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L48', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(-234002.078125, -183920.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(-236029.546875, -184227.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(-234040.203125, -183752.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(-235775.484375, -185138.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(-234344.375, -183998.234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K28-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(-234515.125, -184027.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K01-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(-233938.53125, -183849.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(-234440.40625, -183873.765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K21-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(-234538.4375, -183914.671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K06-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(-236482.65625, -184252.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(-235555.03125, -185127.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C11', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(-235919.421875, -185163.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(-235340.171875, -185033.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(-236214.109375, -185195.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(-233891.265625, -183661.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L38', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(-234419.953125, -183987.671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='K16-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(-235932.28125, -184190.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=157, position=mapping.Point(-236286.8125, -185239.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E06', length=20.0, width=18.0, height=8.0, shelter=False))


class Dwyer(Airport):
    id = 11
    name = "Dwyer"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3775000, vhf_low_hz=38450000, vhf_high_hz=121750000, uhf_hz=343000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-319375.65625, -198386.84375, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield11_0'))
        self.runways.append(Runway(id=1, name='05-23', main=RunwayApproach(name='05', heading=50, beacons=[]), opposite=RunwayApproach(name='23', heading=230, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-319345.625, -198709.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-319739.78125, -199147.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-319329.65625, -198690.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-319396.34375, -198765.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-319457.96875, -198844.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-319377.84375, -198748.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-319759.3125, -199173.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-319364.21875, -198727.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-319779.96875, -199199.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-319444.21875, -198823.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-319425.75, -198806.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-319476.59375, -198861.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-320064.5625, -199421.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-319540.09375, -198990.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-319313.5625, -198671.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-319800.65625, -199225.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-319412.15625, -198784.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-319718.71875, -199122.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-319695.9375, -199097.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-319839.84375, -199278.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-319588.96875, -199047.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-319297.34375, -198652.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-320112.46875, -199381.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-319821.125, -199251.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))


class Nimroz(Airport):
    id = 12
    name = "Nimroz"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=118050000, uhf_hz=250000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-333722.703125, -389854, terrain), terrain)

        self.runways.append(Runway(id=None, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-333800.95881678, -389983.25957064, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-333835.875, -389952.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-333822.49419867, -389972.3684735, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))


class Camp_Bastion_Heliport(Airport):
    id = 13
    name = "Camp Bastion Heliport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4100000, vhf_low_hz=39100000, vhf_high_hz=118200000, uhf_hz=250200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-234602.5, -185373.351563, terrain), terrain)

        self.runways.append(Runway(id=1, name='01-19', main=RunwayApproach(name='01', heading=10, beacons=[]), opposite=RunwayApproach(name='19', heading=190, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-234186.4375, -185496.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PGS03-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-234515.046875, -185525.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN01-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-234653.625, -185528.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN10-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-234562.5, -185463.328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN07-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-234168.96875, -185420.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PGS05-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-234249.046875, -185505.921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PGS01-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-234826.0625, -185566.265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN12-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-234199.125, -185425.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PGS06-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-234624.28125, -185523.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN09-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-234533.75, -185422.921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN04-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-234289.8125, -185440.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PGS09-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-234499.609375, -185180.640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='TRJ05-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-234217.953125, -185501.296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PGS02-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-234157.375, -185491.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PGS04-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-234836.671875, -185497.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN14-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-234345.96875, -185227.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='TRJ01-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-234527.28125, -185457.140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN03-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-234521.109375, -185491.671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN02-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-234486.609375, -185251.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='TRJ04-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-234556.203125, -185497.921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN06-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-234679.3125, -185534.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN11-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-234549.84375, -185531.734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN05-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-234417.296875, -185240.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='TRJ03-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-234695.296875, -185289.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='TRJ08-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-234556.453125, -185264.546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='TRJ06-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-234228.984375, -185431.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PGS07-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-234568.578125, -185428.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN08-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-234259.65625, -185435.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PGS08-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-234832.109375, -185532.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='ARN13-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-234627.25, -185276.203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='TRJ07-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-234320.328125, -185448, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PGS10-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-234382.203125, -185233.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='TRJ02-H', length=18.0, width=15.0, height=8.0, shelter=False))


class Shindand_Heliport(Airport):
    id = 14
    name = "Shindand Heliport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38750000, vhf_high_hz=121500000, uhf_hz=344000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-62917.259766, -368183.640625, terrain), terrain)

        self.runways.append(Runway(id=1, name='36-18', main=RunwayApproach(name='36', heading=360, beacons=[]), opposite=RunwayApproach(name='18', heading=180, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-62854.6328125, -367852.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-62790.19921875, -368002.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-63104.29296875, -367872, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='36', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-62789.421875, -368026.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-63001.9609375, -367924.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='33', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-62927.296875, -367996.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='22', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-62795.890625, -367861.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-63096.9140625, -368041.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='42', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-62792.99609375, -367933.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-62932.2734375, -367878.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='27', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-63101.1484375, -367956.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='39', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-62929.359375, -367949.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='24', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-63099.99609375, -367984.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='40', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-62998.73046875, -367980.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='31', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-62851.82421875, -367946.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-62794.0703125, -367909.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-62854.01171875, -367875.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-62933.3671875, -367855.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='28', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-62997.4765625, -368008.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='30', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-63004.84375, -367867.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='34', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-63003.53515625, -367896.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='34', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-62788.828125, -368056.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-62848.6171875, -368040.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='19', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-63103.875, -367900.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='37', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-62853.3203125, -367899.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-62851.20703125, -367969.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-62930.515625, -367925.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='25', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-62849.37109375, -368016.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='18', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-63102.51171875, -367928.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='38', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-62928.328125, -367972.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='23', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-63098.390625, -368012.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='41', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-62797.08984375, -367834.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-62791.1328125, -367979.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-62852.375, -367922.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-62792.16015625, -367956.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-62794.88671875, -367886.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-63000.73828125, -367952.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='32', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-62926.328125, -368019.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='21', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-62925.05859375, -368043.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='20', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-62931.36328125, -367902.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='26', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-62996.2734375, -368037, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='29', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-62850.3125, -367993.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='17', length=20.0, width=17.0, height=8.0, shelter=False))


class Kandahar_Heliport(Airport):
    id = 15
    name = "Kandahar Heliport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3950000, vhf_low_hz=38800000, vhf_high_hz=119500000, uhf_hz=300200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-268832.328125, -29906.06543, terrain), terrain)

        self.runways.append(Runway(id=1, name='23R-5L', main=RunwayApproach(name='23R', heading=230, beacons=[]), opposite=RunwayApproach(name='5L', heading=50, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-269529.03125, -30147.068359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST19-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-269047.25, -29853.416015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST66-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-268852.03125, -29437.126953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST83-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-269373.46875, -30342.509765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST05-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-268854.09375, -29663.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST75-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-268783.78125, -29492.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST85-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-269082.03125, -29826.234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST67-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-269338.6875, -30233.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST28-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-269366.25, -30006.77734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST57-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-269177.40625, -30145.58203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST48-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-269529.34375, -30228.939453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST17-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-269437.375, -30058.140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST43-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-269205.84375, -30228.53515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST21-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-269255.25, -30296.369140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST20-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-269032, -29757.86328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST72-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-268815.5625, -30078.630859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST59-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-269068.1875, -29732.677734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST71-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-269013.71875, -29882.083984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST65-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-268924.28125, -29610.6015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST77-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-269359.90625, -30217.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST30-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-269401.3125, -30185.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST34-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-269240.25, -30099.353515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST51-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-269198.46875, -30129.92578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST49-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-269451.9375, -30285.93359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST11-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-269392.65625, -30327.736328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST06-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-268889.21875, -29637.18359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST76-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-268995.375, -29782.365234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST73-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-268738.4375, -29971.572265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST62-H', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-269349.09375, -30269.3203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST07-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-269318, -30248.677734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST26-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-269442.65625, -30154.865234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST38-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-269219.5625, -30114.517578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST50-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-269387.6875, -29990.751953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST58-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-269509.90625, -30242.951171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST15-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-269412.65625, -30314.4296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST08-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-269468, -30186.072265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST16-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-269457.5, -30045.44140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST45-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-269117.6875, -29800.392578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST68-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-268839.34375, -29568.931640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST80-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-269309.90625, -30297.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST04-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-269103.40625, -29706.509765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST70-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-269324.34375, -30037.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST55-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-269280.9375, -30069.5234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST53-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-269269.34375, -30182.50390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST27-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-268873.625, -29541.15234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST81-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-268790.875, -30042.20703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST60-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-268908.875, -29514.73046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST82-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-268748.375, -29518.955078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST86-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-269421.6875, -30170.150390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST36-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-269505.28125, -30110.1171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST44-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-269490.6875, -30257.599609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST14-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-269156.3125, -30161.11328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST47-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-269290.5, -30167.955078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST29-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-269227.59375, -30214.107421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST23-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-269352.75, -30119.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST35-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-268766.5, -30005.396484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST61-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-269388.8125, -30241.572265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST10-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-268805.1875, -29596.396484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST79-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-269485.28125, -30124.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST42-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-269135.5625, -30175.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST46-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-269261.46875, -30083.69921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST52-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-269432.21875, -30300.294921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST09-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-269549.3125, -30214.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST18-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-269394.375, -30089.416015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST39-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-268960.8125, -29809.501953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST74-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-268712.40625, -29936.068359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST63-H', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-269415.4375, -30074.1953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST41-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-269153.5, -29775.27734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST69-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-269248.78125, -30198.369140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST25-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-268818.09375, -29464.44921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST84-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-269463.59375, -30139.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST40-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-269303.625, -30053.00390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST54-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-269354.15625, -30357.09765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST03-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-269373.34375, -30104.68359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST37-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-269275.34375, -30279.37109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST22-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-269297.0625, -30264.12109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST24-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-269428.78125, -30214.404296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST13-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-269335.09375, -30371.833984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST02-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-269315.9375, -30385.8359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST01-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-268959.625, -29584.396484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST78-H', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-268685.71875, -29901.119140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST64-H', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-269379.25, -30203.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST32-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-269345.15625, -30022.185546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST56-H', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-269471.0625, -30271.755859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST12-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-269311.40625, -30151.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST31-H', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-269330.3125, -30136.783203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='MST33-H', length=20.0, width=17.0, height=8.0, shelter=False))


ALL_AIRPORTS: List[Type[Airport]] = [
    Herat,
    Farah,
    Shindand,
    Maymana_Zahiraddin_Faryabi,
    Chaghcharan,
    Qala_i_Naw,
    Kandahar,
    Bost,
    Tarinkot,
    Camp_Bastion,
    Dwyer,
    Nimroz,
    Camp_Bastion_Heliport,
    Shindand_Heliport,
    Kandahar_Heliport,
]

