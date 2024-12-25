# flake8: noqa
from typing import List, Type

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


class Al_Asad_Airbase(Airport):
    id = 1
    name = "Al-Asad Airbase"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3900000, vhf_low_hz=38700000, vhf_high_hz=131200000, uhf_hz=363700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(60818.751953, -165901.171875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield1_0'))
        self.runways.append(Runway(id=1, name='09L-27R', main=RunwayApproach(name='09L', heading=90, beacons=[RunwayBeacon(id='airfield1_1', runway_name='09L-27R', runway_id=1, runway_side='09L'), RunwayBeacon(id='airfield1_3', runway_name='09L-27R', runway_id=1, runway_side='09L')]), opposite=RunwayApproach(name='27R', heading=270, beacons=[RunwayBeacon(id='airfield1_2', runway_name='09L-27R', runway_id=1, runway_side='27R'), RunwayBeacon(id='airfield1_4', runway_name='09L-27R', runway_id=1, runway_side='27R')])))
        self.runways.append(Runway(id=2, name='09R-27L', main=RunwayApproach(name='09R', heading=90, beacons=[]), opposite=RunwayApproach(name='27L', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(62287.862660141, -161131.36123982, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(62288.378285141, -161192.00186482, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(62288.065785141, -161241.14248982, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(62171.055304049, -161153.37401595, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(62171.055304049, -161202.49901595, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(62171.051397799, -161303.73339095, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(62171.051397799, -161252.73339095, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(62215.844936877, -161465.81631872, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(62224.28001828, -161555.78417573, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(62215.043890636, -161645.94689239, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(62214.040261239, -161691.29890754, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(62214.561737823, -161736.46346263, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(62218.754687546, -161825.82047149, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(62232.7578125, -162605.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(62233.09765625, -162559.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(62233.3984375, -162513.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(62233.25, -162468.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(62135.1796875, -162579.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(62135.69140625, -162550.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(62136.08984375, -162521.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(62136.6015625, -162492.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(62358.7578125, -163717.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(62358.5078125, -163678.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(62358.453125, -163638.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(62358.203125, -163598.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(62358.4453125, -163552.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(62358.091634647, -163508.41917153, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(62358.019298657, -163463.0071321, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(62357.953861329, -163425.07555299, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(62132.47265625, -164391.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='63', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(62097.15234375, -164391.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='64', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(62169.6796875, -164459.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='60', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(62136.640625, -164459.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='61', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(62104.03515625, -164458.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='62', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(62164.86328125, -164555.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='52', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(62140.5703125, -164555.515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='53', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(62117.77734375, -164555.515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='54', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(62093.171875, -164555.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='55', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(62092.95703125, -164515.640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='59', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(62117.25390625, -164515.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='58', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(62140.046875, -164515.671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='57', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(62164.6484375, -164515.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='56', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(62205.72265625, -165156.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(62174.31640625, -165155.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(62143.27734375, -165155.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(62144.15234375, -165083.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(62175.55859375, -165084.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(62206.6015625, -165083.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(62215.19140625, -165010.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(62195.99609375, -165009.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(62176.7421875, -165009.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(62157.546875, -165009, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(62138.4140625, -165008.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(62137.8515625, -165054.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(62157.04296875, -165055.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(62176.296875, -165055.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(62195.48828125, -165056.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(62214.62109375, -165056.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(62138.30859375, -164982.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(62157.5, -164982.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(62176.75390625, -164982.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(62195.9453125, -164983.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(62215.078125, -164983.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(62215.6484375, -164937.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(62196.453125, -164936.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(62177.19921875, -164936.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(62158.00390625, -164936.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(62138.87109375, -164936.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(62206.4375, -164907.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(62175.03515625, -164907.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(62143.9921875, -164907.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(62144.87109375, -164835.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(62176.27734375, -164835.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(62207.31640625, -164835.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(62206.90234375, -164804.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(62175.49609375, -164804.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(62144.453125, -164804.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(63149.859375, -165249.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(63116.61328125, -165138.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(62960.953125, -165301.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(62809.25, -165219.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(62970.98046875, -165120.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(62607.65625, -166209.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(62732.83984375, -166233.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(62539.63671875, -166442.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(62526.20703125, -166430.359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(62700.29296875, -166462.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(62696.875, -166393.640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(62701.91015625, -166375.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(62707.1640625, -166356.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(62712.0546875, -166338.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(62525.10546875, -166513.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(62406.28125, -166504.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(60366.8515625, -164243.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='106', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(60476.0625, -164550.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(60476.8515625, -164590.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(60475.765625, -164630.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(60475.40234375, -164671.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(60475.94921875, -164716.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(60476.30859375, -164760.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(60475.5859375, -164805.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(60053.513894164, -163077.63666924, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='114', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(60366.984375, -163297.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(60197.869086297, -163345.0462942, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(60254.804243084, -163102.09129487, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(60358.0546875, -163493.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='110', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(60295.38671875, -163766.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='108', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(60413.3046875, -163677.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='109', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(60421.046875, -164031.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='107', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(60338.640625, -167967.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(60363.9453125, -167755.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(60415.5, -167580.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(60295.709734721, -167490.3386081, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(60423.11328125, -167223.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))


class Baghdad_International_Airport(Airport):
    id = 2
    name = "Baghdad International Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38750000, vhf_high_hz=118900000, uhf_hz=250300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-142.077148, 159.874573, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield2_1'))
        self.beacons.append(AirportBeacon(id='airfield2_6'))
        self.beacons.append(AirportBeacon(id='airfield2_0'))
        self.runways.append(Runway(id=1, name='15L-33R', main=RunwayApproach(name='15L', heading=150, beacons=[RunwayBeacon(id='airfield2_3', runway_name='15L-33R', runway_id=1, runway_side='15L'), RunwayBeacon(id='airfield2_5', runway_name='15L-33R', runway_id=1, runway_side='15L')]), opposite=RunwayApproach(name='33R', heading=330, beacons=[RunwayBeacon(id='airfield2_2', runway_name='15L-33R', runway_id=1, runway_side='33R'), RunwayBeacon(id='airfield2_4', runway_name='15L-33R', runway_id=1, runway_side='33R')])))
        self.runways.append(Runway(id=2, name='15R-33L', main=RunwayApproach(name='15R', heading=150, beacons=[RunwayBeacon(id='airfield2_7', runway_name='15R-33L', runway_id=2, runway_side='15R'), RunwayBeacon(id='airfield2_10', runway_name='15R-33L', runway_id=2, runway_side='15R')]), opposite=RunwayApproach(name='33L', heading=330, beacons=[RunwayBeacon(id='airfield2_8', runway_name='15R-33L', runway_id=2, runway_side='33L'), RunwayBeacon(id='airfield2_9', runway_name='15R-33L', runway_id=2, runway_side='33L')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-340.89886474609, -195.74822998047, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-373.49673461914, -177.78594970703, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-399.22741699219, -161.52503967285, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-502.87225341797, -87.42308807373, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-546.51654052734, -62.536930084229, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-592.41467285156, -38.74275970459, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-635.76434326172, -14.49162197113, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-681.03173828125, 9.4611101150513, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-729.23419189453, 36.260890960693, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-775.42749023438, 63.83012008667, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-820.74975585938, 86.278861999512, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-864.40075683594, 111.35050964355, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-909.15997314453, 135.45901489258, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-954.09295654297, 159.60916137695, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-998.50946044922, 184.23860168457, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-1042.3616943359, 208.49125671387, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-1085.8344726562, 234.30101013184, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-1128.8160400391, 259.44760131836, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-1172.8331298828, 284.76190185547, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-1216.7592773438, 310.23400878906, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-1261.2260742188, 334.69638061523, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-1304.4731445312, 359.69360351562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-1348.0806884766, 385.58560180664, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-1391.6883544922, 411.16314697266, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-1439.6986083984, 438.41787719727, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-1538.8602294922, 498.4231262207, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-1615.0330810547, 537.43096923828, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(1162.4016113281, -1072.7572021484, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(1135.5523681641, -1056.9897460938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(1108.3115234375, -1042.7017822266, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(1080.7633056641, -1027.958984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(1052.9886474609, -1012.5621948242, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(1025.0629882812, -997.31634521484, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(1103.5568847656, -1114.5993652344, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(1076.6754150391, -1100.01171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(1049.1706542969, -1084.6540527344, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(1021.3480834961, -1068.6739501953, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(994.27673339844, -1053.1888427734, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(966.61437988281, -1037.8288574219, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(933.259765625, -1020.7630615234, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(940.01452636719, -948.25842285156, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(918.52325439453, -935.17913818359, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(795.84033203125, -832.87219238281, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(825.50366210938, -947.41180419922, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(714.94036865234, -779.33917236328, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(689.39971923828, -822.26916503906, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(632.87176513672, -732.54760742188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(607.51226806641, -775.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(541.44519042969, -729.73962402344, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(482.07308959961, -678.62603759766, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(422.03335571289, -662.06079101562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(362.18615722656, -611.21862792969, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(302.86303710938, -594.55261230469, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(242.93612670898, -561.49468994141, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(191.53297424316, -495.15930175781, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(141.67649841309, -467.29440307617, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(168.46485900879, -481.75128173828, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(65.915901184082, -435.33499145508, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(29.516876220703, -415.28958129883, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-86.772041320801, -348.84945678711, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-48.781230926514, -369.94662475586, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(2152.4609375, 672.89459228516, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(2190.1977539062, 650.89215087891, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(2227.5578613281, 629.50769042969, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(474.30892944336, 1638.3605957031, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(435.01336669922, 1660.3579101562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(396.14813232422, 1682.5294189453, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(357.54373168945, 1704.4399414062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(1433.908203125, 838.57427978516, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(1471.1746826172, 774.53979492188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(1509.3924560547, 712.81072998047, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-602.08477792817, 1277.9359129097, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-666.89575204927, 1317.8022459175, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-752.12683105469, 1311.6567382812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-313.2048034668, 609.96734619141, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-161.34635925293, 524.21234130859, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-815.70727539062, 1354.8565673828, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-844.98901367188, 1310.8950195312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-863.455078125, 1278.2541503906, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-669.17820377396, 1145.9881315208, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-708.49981134677, 1168.1491161407, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-747.82632851891, 1189.875777662, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-787.72222900391, 1213.4575195312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-828.35229492188, 1233.9345703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-129.95095825195, 584.17651367188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-110.3070602417, 627.48852539062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-280.47161865234, 668.32250976562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-257.1003112793, 708.54412841797, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(173.11990356445, 640.77325439453, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(136.10208129883, 661.61364746094, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(99.037979125977, 682.36218261719, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(33.446407318115, 740.18255615234, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-5.3562574386597, 761.89562988281, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-45.024265289307, 784.23858642578, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-84.071586608887, 805.94427490234, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-109.96539892714, 867.86049286957, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-147.64368261855, 889.07564179535, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-185.15827002089, 910.04774872894, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-374.7096862793, 980.68267822266, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-415.80731201172, 1005.3188476562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-456.37951660156, 1029.2012939453, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-496.33444213867, 1052.9011230469, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-536.43591308594, 1076.7810058594, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-307.29501342773, 940.68756103516, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(33.791805267334, 518.81414794922, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(76.922569274902, 494.94653320312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(244.43948364258, 373.13354492188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(131.00308227539, 438.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=60.0, width=60.0, height=18.0, shelter=False))


class Erbil_International_Airport(Airport):
    id = 4
    name = "Erbil International Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3950000, vhf_low_hz=38800000, vhf_high_hz=128800000, uhf_hz=250350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(330838.3125, -22360.119141, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield4_0'))
        self.runways.append(Runway(id=2, name='15-33R', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33R', heading=330, beacons=[RunwayBeacon(id='airfield4_5', runway_name='15-33R', runway_id=2, runway_side='33R'), RunwayBeacon(id='airfield4_6', runway_name='15-33R', runway_id=2, runway_side='33R')])))
        self.runways.append(Runway(id=1, name='18-36', main=RunwayApproach(name='18', heading=180, beacons=[RunwayBeacon(id='airfield4_2', runway_name='18-36', runway_id=1, runway_side='18'), RunwayBeacon(id='airfield4_4', runway_name='18-36', runway_id=1, runway_side='18')]), opposite=RunwayApproach(name='36', heading=360, beacons=[RunwayBeacon(id='airfield4_1', runway_name='18-36', runway_id=1, runway_side='36'), RunwayBeacon(id='airfield4_3', runway_name='18-36', runway_id=1, runway_side='36')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(331475.59375, -21074.541015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(331447.25, -21059.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(331418.53125, -21044.349609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(331390.5, -21029.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(331305, -20984.619140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(331361.75, -21014.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(331333.0625, -20999.349609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(331275.625, -20969.75390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(331315.15625, -20902.013671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(331349.5625, -20919.654296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(331383.5, -20937.33984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(331451.53125, -20973.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(331417.5625, -20955.416015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(331519.25, -21008.54296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(331485.96875, -20991.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(331089.0625, -20822.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(330039.5, -20213.51953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(331043.25, -20798.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(330997.28125, -20775.150390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(330949.59375, -20750.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(330061.125, -20225.412109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(330082.0625, -20236.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(330515.71875, -20434.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(330487.65625, -20420.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(330459.1875, -20404.818359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(330431.5625, -20389.603515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(330403.96875, -20375.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(330352.125, -20342.931640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='48', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(330321.90625, -20327.498046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='49', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(330293.4375, -20312.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='50', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(330267.0625, -20299.26171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='51', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(330239.53125, -20284.89453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='52', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(330768.65625, -20534.953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='40', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(330753.09375, -20565.97265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='39', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(330687.78125, -20546.970703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='41', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(330655.53125, -20531.810546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='42', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(329968.625, -20591.5703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='65', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(329955.40625, -20616.677734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='66', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(329941.8125, -20642.451171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='67', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(329692.6875, -20569.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(329737.46875, -20592.783203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(329782.875, -20615.947265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(329828.5625, -20639.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(329873.96875, -20662.271484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(329510.84375, -20170.458984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='79', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(329535.4375, -20182.95703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='78', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(329646.30113443, -20457.31555737, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='76', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(329684.22746945, -20490.641871042, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='75', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(329615.05531557, -20443.55301266, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='77', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(329870.1875, -20537.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(329818.84375, -20509.990234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(329994.5625, -21745.220703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(330063.03125, -21744.794921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(329926.0625, -21745.267578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(330131.53125, -21744.224609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(330202.40625, -21744.048828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(330271.90625, -21744.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(330342.90625, -21744.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(330413.8125, -21744.576171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(330483, -21743.623046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(330552, -21742.287109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='9', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(330618.96875, -21743.564453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='8', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(329853.40625, -21745.009765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(330718.90625, -21732.423828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='7', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(330719.84375, -21780.455078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='6', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(331184.46875, -21735.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='5', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(331248.90625, -21736.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='4', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(331313.90625, -21735.701171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='3', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(331379.78125, -21735.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='2', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(331444.9375, -21735.798828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='1', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(329791.375, -20994.6171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='62', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(329883.09375, -20928.330078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='61', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(329884.9375, -20815.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='60', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(329728.65625, -20911.99609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='63', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(329710, -20902.111328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='64', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(330621.0625, -21145.16015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(330572.15625, -21118.087890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(330524.71875, -21095.06640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(330476.1875, -21069.087890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=40.0, width=40.0, height=12.0, shelter=False))


class Bashur_Airport(Airport):
    id = 5
    name = "Bashur Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3975000, vhf_low_hz=38850000, vhf_high_hz=118800000, uhf_hz=250400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(363380.050179, 13139.524874, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield5_0'))
        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[]), opposite=RunwayApproach(name='31', heading=310, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(362660.6875, 13591.611328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='1', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(362542.71875, 13688.470703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='4', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(362581.28125, 13654.798828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='3', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(362620.625, 13622.411132812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='2', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(362377.09375, 13649.16015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='9', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(362395.3125, 13632.697265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='8', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(362432.5, 13599.619140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='6', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(362413.40625, 13615.901367188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='7', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(362474.09375, 13621.08203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='5', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(362388.65625, 13694.674804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(362386.375, 13734.596679688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(362404.78125, 13757.170898438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(362424.125, 13779.559570312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(362444.125, 13802.600585938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(362463.78125, 13826.177734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))


class Qayyarah_Airfield_West(Airport):
    id = 6
    name = "Qayyarah Airfield West"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4000000, vhf_low_hz=38900000, vhf_high_hz=122200000, uhf_hz=250450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(279543.921875, -97449.582031, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield6_0'))
        self.runways.append(Runway(id=1, name='15-33', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33', heading=330, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(280360.0625, -98266.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(280294.59375, -98235.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(280062.125, -98111.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(280104.3125, -98131.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(280146.6875, -98150.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(280188.34375, -98170.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(280251.78125, -98205.640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(280224, -98191.6484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(278190.8125, -97182.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(278224.03125, -97207.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(278353.4375, -97269.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(278309.34375, -97247.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(278267.125, -97226.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(278165.15625, -97170.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(278139.6875, -97157.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(278041.28125, -97116.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(278113.0625, -97144.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(278086.9375, -97131.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(278991.65625, -97752.8046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(278974.53125, -97744.4609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(278957.15625, -97735.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(278939.5, -97727.1015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(278920.75, -97717.296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(278901.75, -97708.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(278879.40625, -97696.7734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(278853.90625, -97684.0859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(278827.9375, -97671.7109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(278797.75, -97654.8046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='18', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(278760.90625, -97635.7890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='19', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(278723.75, -97617.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='20', length=42.0, width=34.0, height=14.0, shelter=False))


class Sulaimaniyah_International_Airport(Airport):
    id = 7
    name = "Sulaimaniyah International Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4025000, vhf_low_hz=38950000, vhf_high_hz=121700000, uhf_hz=250500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(255225.726563, 100814.4375, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield7_4'))
        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[RunwayBeacon(id='airfield7_1', runway_name='13-31', runway_id=1, runway_side='13'), RunwayBeacon(id='airfield7_2', runway_name='13-31', runway_id=1, runway_side='13')]), opposite=RunwayApproach(name='31', heading=310, beacons=[RunwayBeacon(id='airfield7_3', runway_name='13-31', runway_id=1, runway_side='31'), RunwayBeacon(id='airfield7_0', runway_name='13-31', runway_id=1, runway_side='31')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(256650.875, 99939.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(256605.78125, 99989.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(256563.234375, 100036.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(256522.140625, 100082.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(256483.328125, 100126.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(256444.15625, 100167.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(255293.3125, 101391.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(255270.9375, 101414.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(255248.53125, 101437.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(255225.5, 101461.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(255201.8125, 101485.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(255179.421875, 101510.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(254964.19026852, 101868.01560479, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(255022.441851, 101806.23417696, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(255070.1833462, 101751.75286754, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(255119.75, 101714.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(254689.21875, 102208.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(254674.515625, 102194.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(254659.8125, 102180.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(254644.5625, 102166.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(254629.328125, 102152.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(254718.734375, 102329.078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='22', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(254706.234375, 102343.0546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='23', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(254694.015625, 102357.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='24', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(254714.625, 102362.5390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='25', length=18.0, width=15.0, height=8.0, shelter=False))


class Balad_Airbase(Airport):
    id = 8
    name = "Balad Airbase"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4050000, vhf_low_hz=39000000, vhf_high_hz=119800000, uhf_hz=250550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(75938.074219, 13806.166504, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield8_0'))
        self.runways.append(Runway(id=1, name='12-30', main=RunwayApproach(name='12', heading=120, beacons=[]), opposite=RunwayApproach(name='30', heading=300, beacons=[])))
        self.runways.append(Runway(id=2, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(75310.796875, 14708.974609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(75382.7734375, 14669.864257812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(75317.9140625, 12241.33203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='135', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(75368.2421875, 12171.38671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='134', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(77186.5078125, 13422.615234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(77347.75, 13634.485351562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(77302.6484375, 13565.633789062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(77280.7265625, 13530.763671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(77258.296875, 13495.811523438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(77235.0859375, 13460.076171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(77393.4375, 13296.750976562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(77365.703125, 13316.911132812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(77336.75, 13334.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(77619.8984375, 13777.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(77602.1875, 13751.500976562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(77458.3125, 13824.008789062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(77475.8046875, 13850.387695312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(77491.09375, 13877.157226562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(77508.5859375, 13903.536132812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(77523.2734375, 13927.478515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(77540.765625, 13953.857421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(77177.484375, 13338.383789062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='21', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(77147.25, 13357.662109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(77116.9453125, 13378.62109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(76672.671875, 11801.178710938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(76709.9453125, 11758.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(76753.671875, 11718.08203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(76813.4375, 11787.358398438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(76773.0546875, 11828.51171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(76729.3359375, 11865.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(75267.5078125, 12300.059570312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='136', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(75196.328125, 12398.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='137', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(75163.4296875, 12444.688476562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='138', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(75429.6953125, 12084.98046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='133', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(77351.6171875, 12194.787109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(76629.778985799, 14205.783902538, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(76614.821149956, 14215.76183789, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(76600.342990908, 14225.565739129, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(76585.562320652, 14236.044730772, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(76568.557708653, 14247.873104307, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(76555.851714532, 14256.739420368, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(76540.972256266, 14267.152393211, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(75459.078125, 14676.848632812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(75441.2734375, 14689.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(75423.3515625, 14701.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(75405.09375, 14713.19921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(75386.5078125, 14725.41015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(75368.3515625, 14737.857421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(75350.4296875, 14750.172851562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(75331.765625, 14762.31640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(75402.734375, 14935.043945312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(75439.078125, 14886.118164062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(75414.53125, 14847.391601562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(75389.71875, 14807.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(75464.25, 14761.548828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(75486.339102108, 14798.268468298, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(75510.625791152, 14837.978194315, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(75560.4453125, 14734.395904501, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(75587.874077497, 14774.615107506, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(75619.330954158, 14823.236916294, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(75424.3125, 14633.580078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(75459.96875, 14608.967773438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(75492.8125, 14644.15234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(75124.133010542, 14857.340511295, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(75147.18492901, 14859.76939535, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(75247.5859375, 15141.051757812, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(75382.7890625, 15283.963867188, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(75159.8046875, 15362.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(75026.6171875, 15209.130859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(74679.5234375, 15335.758789062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(74658.75, 15534.7578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(74466.1640625, 15410.91015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(74444.71875, 15610.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(74766.984375, 15192.982421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(74692.1875, 15076.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(74869.8515625, 15043.500976562, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(74969.9609375, 14884.13671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(74683.8671875, 14791.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(74681.484375, 14810.383789062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(74678.8671875, 14829.944335938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(74676.9140625, 14850.364257812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(74561.15625, 15151.802734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(74536.2734375, 15149.149414062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(74510.6640625, 15146.799804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(74485.8828125, 15144.661132812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(74460.34375, 15142.397460938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(74434.9375, 15139.880859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(74553.8515625, 15216.619140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(74529.234375, 15214.525390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(74503.2734375, 15211.959960938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(74478.515625, 15209.543945312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(74452.5546875, 15206.978515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(74428.1015625, 15204.260742188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(74102.55923654, 13798.057876694, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='174', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(74108.26364712, 13820.136594973, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='175', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(74417.625, 13473.126953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='167', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(74388.8203125, 13510.159179688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='168', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(74361.7421875, 13549.533203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='169', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(74332.796875, 13587.556640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='170', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(74304.3203125, 13627.787109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='171', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(74276.375, 13667.001953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='172', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(74247.078125, 13706.21484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='173', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(73696.1875, 14486.395507812, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='191', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(73508.053303238, 14526.065911144, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='190', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(73552.9140625, 14303.259765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='187', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(73315.1328125, 14404.040039062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='189', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(73709.75, 14586.081054688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='192', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(73695.1875, 14605.883789062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='193', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(73679.5234375, 14626.171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='194', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(73665.5625, 14646.729492188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='195', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(73649.6953125, 14666.669921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='196', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(73635.125, 14686.47265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='197', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(73604.564378859, 14728.366618976, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='199', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(73618.420490399, 14707.913827749, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='198', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(73590.484375, 14747.530273438, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='200', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(73575.00411493, 14769.03157661, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='201', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(73560.2578125, 14787.62109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='202', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(73497.7890625, 14741.845703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='212', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(73512.128164439, 14721.952840738, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='211', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(73526.97329904, 14701.490617658, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='210', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(73540.684730798, 14682.048284356, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='209', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(73555.607298098, 14662.336061277, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='208', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(73586.4609375, 14619.674804688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='206', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(73572.671875, 14640.346679688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='207', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(73601.3203125, 14599.338867188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='205', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(73615.71875, 14579.416992188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='204', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(73630.04620461, 14560.091937084, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='203', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(73508.0859375, 14791.685546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='213', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(74101.390625, 13977.6640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='176', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(73977.4921875, 14155.877929688, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='177', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(73771.96875, 14134.751953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='181', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(73776.75, 14281.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='182', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(73609.8984375, 14152.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='186', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(73387.71875, 14373.290039062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='188', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(73875.6796875, 14375.97265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='183', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(73848.6796875, 14382.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='184', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(73822.28125, 14390.52734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='185', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(73847.671875, 14056.250976562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='180', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(73910.7890625, 14050.681640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='179', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(73963.6796875, 14045.428710938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='178', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(76865.6171875, 12027.477539062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(76811.875, 11973.028320312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(76917.2578125, 12082.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(76971.5078125, 12138.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(77105.3828125, 12504.978515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(75135.0390625, 12481.935546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='139', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(75108.7734375, 12516.873046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='140', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(75083.9375, 12552.701171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='141', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(75058.375, 12587.392578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='142', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(75030.828125, 12621.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='143', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(75005.15625, 12657.321289062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='144', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(74978.890625, 12691.556640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='145', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(74952.4453125, 12727.060546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='146', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=157, position=mapping.Point(74926.359375, 12764.737304688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='147', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=158, position=mapping.Point(74898.6953125, 12803.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='148', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=159, position=mapping.Point(74878.7890625, 12836.87890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='149', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=160, position=mapping.Point(74860.3046875, 12862.674804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='150', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=161, position=mapping.Point(74842.8125, 12886.42578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='151', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=162, position=mapping.Point(74823.9765625, 12912.104492188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='152', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=163, position=mapping.Point(74806.5703125, 12936.717773438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='153', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=164, position=mapping.Point(74788.109375, 12961.555664062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='154', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=165, position=mapping.Point(74770.1328125, 12987.697265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='155', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=166, position=mapping.Point(74750.234375, 13014.643554688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='156', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=167, position=mapping.Point(74730.96875, 13041.006835938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='157', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=168, position=mapping.Point(74712.515625, 13065.844726562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='158', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=169, position=mapping.Point(74694.5390625, 13091.987304688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='159', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=170, position=mapping.Point(74674.6328125, 13118.93359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='160', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=171, position=mapping.Point(74654.125, 13147.33203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='161', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=172, position=mapping.Point(74635.671875, 13172.169921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='162', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=173, position=mapping.Point(74617.6953125, 13198.311523438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='163', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=174, position=mapping.Point(74597.7890625, 13225.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='164', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=175, position=mapping.Point(74577.6640625, 13251.399414062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='165', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=176, position=mapping.Point(74559.6875, 13277.541992188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='166', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=177, position=mapping.Point(75467.453125, 12021.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='132', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=178, position=mapping.Point(75495.0859375, 11980.60546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='131', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=179, position=mapping.Point(75522.9453125, 11942.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='130', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=180, position=mapping.Point(75551.109375, 11901.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='129', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=181, position=mapping.Point(75579.0078125, 11861.728515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='128', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=182, position=mapping.Point(75604.8828125, 11824.540039062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='127', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=183, position=mapping.Point(75631.6171875, 11787.370117188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='126', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=184, position=mapping.Point(75828.5625, 11596.01171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='125', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=185, position=mapping.Point(75842.984375, 11296.850585938, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='124', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=186, position=mapping.Point(75956.890625, 11409.5390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='123', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=187, position=mapping.Point(76043.1484375, 11084.103515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='118', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=188, position=mapping.Point(76122.140625, 11135.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=189, position=mapping.Point(76130.125, 11165.93359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=190, position=mapping.Point(76137.734375, 11196.184570312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=191, position=mapping.Point(76146.265625, 11227.813476562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=192, position=mapping.Point(76152.53125, 11258.48828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=193, position=mapping.Point(76024.2265625, 11314.643554688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='122', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=194, position=mapping.Point(76016.5, 11284.385742188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='121', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=195, position=mapping.Point(76009.140625, 11254.07421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='120', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=196, position=mapping.Point(76000.8671875, 11222.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='119', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=197, position=mapping.Point(77720.546875, 13536.493164062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=198, position=mapping.Point(77740.4609375, 13335.247070312, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=199, position=mapping.Point(77941.0703125, 13457.876953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=200, position=mapping.Point(77914.359375, 13658.350585938, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=201, position=mapping.Point(78395.1484375, 12968.067382812, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=202, position=mapping.Point(78192.5390625, 12951.174804688, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=203, position=mapping.Point(78119.1171875, 12732.598632812, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=204, position=mapping.Point(78284.6953125, 12747.166992188, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=205, position=mapping.Point(77976.390625, 12895.924804688, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=206, position=mapping.Point(77974.28125, 13041.120117188, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=207, position=mapping.Point(77827.671875, 12950.952148438, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=208, position=mapping.Point(77644.1953125, 13078.6328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=209, position=mapping.Point(77612.09375, 13221.198242188, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=210, position=mapping.Point(77610.03125, 13244.673828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=211, position=mapping.Point(77635.4296875, 13800.762695312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=212, position=mapping.Point(77651.890625, 13825.448242188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=213, position=mapping.Point(77667.9765625, 13851.315429688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=214, position=mapping.Point(77894.28125, 12772.288085938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=215, position=mapping.Point(77866.171875, 12769.932617188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=216, position=mapping.Point(77837.640625, 12767.215820312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))


class Al_Taji_Airport(Airport):
    id = 9
    name = "Al-Taji Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4075000, vhf_low_hz=39050000, vhf_high_hz=126000000, uhf_hz=250600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(29547.012482, 3272.628293, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield9_0'))
        self.runways.append(Runway(id=None, name='34-16', main=RunwayApproach(name='34', heading=340, beacons=[]), opposite=RunwayApproach(name='16', heading=160, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(30121.892578125, 3172.6245117188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(30241.546875, 3131.1926269531, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(30296.962890625, 3112.7756347656, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(30354.88671875, 3092.1105957031, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(28636.640625, 3378.2839355469, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(28579.203125, 3395.5319824219, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(28523.552734375, 3412.4799804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(30392.451171875, 3154.6782226562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(30402.173828125, 3185.6240234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(30331.796875, 3174.0659179688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(30368.046875, 3277.5083007812, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(30358.763671875, 3249.6179199219, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(30298.626953125, 3273.3720703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(30308.322265625, 3301.5986328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(30282.408203125, 3220.1772460938, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(30273.107421875, 3193.1071777344, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(30213.115234375, 3213.4526367188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(30222.119140625, 3240.7795410156, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(30238.416015625, 3292.7482910156, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(30248.67578125, 3321.5275878906, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(30152.078125, 3234.5808105469, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(30161.830078125, 3261.9519042969, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(30075.662109375, 3275.08203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='21', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(29798.958984375, 3351.4248046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='22', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(29808.3125, 3377.3203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='23', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(29817.11328125, 3404.0102539062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='24', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(29826.50390625, 3431.8679199219, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='25', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(29835.435546875, 3457.4985351562, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='26', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(29801.3125, 3469.1735839844, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='31', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(29793.123046875, 3443.4846191406, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='30', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(29783.41015625, 3415.7153320312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='29', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(29774.974609375, 3389.2302246094, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='28', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(29765.693359375, 3362.6689453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='27', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(29699.0078125, 3385.2138671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='32', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(29707.771484375, 3411.1936035156, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='33', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(29717.162109375, 3437.7993164062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='34', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(29726.552734375, 3465.6569824219, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='35', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(29735.5703125, 3491.6076660156, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='36', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(29616.35546875, 3442.62890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='43', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(29625.744140625, 3469.2346191406, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='44', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(29635.134765625, 3497.0922851562, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='45', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(29643.900390625, 3522.1330566406, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='46', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(29607.58984375, 3416.6491699219, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='42', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(29266.896484375, 3173.41796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='48', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(29240.267578125, 3183.0568847656, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='49', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(29215.388671875, 3192.2524414062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='50', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(29189.677734375, 3201.2331542969, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='51', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(29290.5234375, 3165.0734863281, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='47', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(29166.40234375, 3211.3037109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='52', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(29142.7734375, 3219.6479492188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='53', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(29118.12109375, 3228.1923828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='54', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(29102.490234375, 3195.8542480469, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='55', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(29127.716796875, 3187.6318359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='56', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(29152.419921875, 3181.1057128906, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='57', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(29177.59765625, 3172.8344726562, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='58', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(29202.056640625, 3164.3286132812, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='59', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(29023.42578125, 3202.8947753906, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='60', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(28948.83203125, 3284.1923828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='61', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(28924.6171875, 3293.0112304688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='62', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(28900.7265625, 3301.6164550781, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='63', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(28876.96875, 3310.2119140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='64', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(28853.052734375, 3319.3286132812, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='65', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(28828.361328125, 3327.9987792969, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='66', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(28804.0703125, 3334.986328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='67', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(28780.44140625, 3343.3305664062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='68', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(28756.68359375, 3352.4482421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='69', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(28732.587890625, 3360.6003417969, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='70', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(28708.44140625, 3368.7546386719, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='71', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(28692.67578125, 3334.9763183594, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='72', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(28718.41015625, 3326.2917480469, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='73', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(28743.23828125, 3317.3234863281, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='74', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(28767.53515625, 3308.7875976562, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='75', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(28791.86328125, 3300.3562011719, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='76', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(28815.974609375, 3291.8798828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='77', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(28841.173828125, 3285.0231933594, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='78', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(28864.9765625, 3276.6586914062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='79', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(28888.669921875, 3267.9411621094, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='80', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(28912.81640625, 3259.0876464844, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='81', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(28938.779296875, 3250.1306152344, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='82', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(28884.4296875, 3171.2890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='83', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(28860.802734375, 3179.6333007812, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='84', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(28836.3046875, 3188.4030761719, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='85', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(28811.42578125, 3197.5986328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='86', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(28786.107421875, 3205.9704589844, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='87', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(28762.154296875, 3214.599609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='88', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(28736.826171875, 3222.8239746094, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='89', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(28712.33984375, 3231.4604492188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='90', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(28687.4609375, 3240.6560058594, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='91', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(28662.3515625, 3249.5969238281, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='92', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(28621.380859375, 3269.1650390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='93', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(28597, 3276.9453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='94', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(28573.37109375, 3285.2897949219, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='95', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(28548.509765625, 3294.1489257812, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='96', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(29707.423828125, 3501.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='41', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(29699.236328125, 3475.6547851562, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='40', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(29689.5234375, 3447.8854980469, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='39', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(29681.087890625, 3421.400390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='38', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(29671.806640625, 3394.8391113281, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='37', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(30179.30078125, 3153.4272460938, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.0, width=23.0, height=10.0, shelter=False))


class Kirkuk_International_Airport(Airport):
    id = 10
    name = "Kirkuk International Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3775000, vhf_low_hz=38450000, vhf_high_hz=125550000, uhf_hz=250050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(245433.733046, 12825.298765, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield10_1'))
        self.beacons.append(AirportBeacon(id='airfield10_0'))
        self.runways.append(Runway(id=2, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[]), opposite=RunwayApproach(name='31', heading=310, beacons=[RunwayBeacon(id='airfield10_2', runway_name='13-31', runway_id=1, runway_side='31'), RunwayBeacon(id='airfield10_3', runway_name='13-31', runway_id=1, runway_side='31')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(246241.06052161, 11527.119247189, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(246549.37380783, 12361.466072292, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(246333.2101928, 12423.337358912, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(246122.859375, 12383.676757812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(246090.41223278, 12607.703506873, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(244312.40625, 14621.127929688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(244157.01622842, 14679.46512784, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(244031.52506617, 14697.700764066, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(246182.81079846, 11684.309166612, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(246089.62440659, 11572.344771193, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(246028.60729583, 11399.699950661, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(245824.47735027, 11473.856341918, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(245759.41143519, 11637.338722936, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(245609.60521696, 11702.426673616, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(246037.27234911, 11867.688410009, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(245767.34375, 12031.639648438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(245658.796875, 11929.018554688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(245694.671875, 11963.05859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(245729.609375, 11998.366210938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(245807.484375, 11819.629882812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(245831.546875, 11794.407226562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(245856.171875, 11768.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(245880.46875, 11742.883789062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(245904.515625, 11717.66015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(245929.15625, 11691.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(245954.0625, 11665.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(244772.234375, 14292.29296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(244731.875, 14321.229492188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(244690.1875, 14350.151367188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(244648.5, 14379.823242188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(244606.046875, 14409.12109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(244567.09375, 14437.309570312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(244489.75, 13560.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(244462.890625, 13578.85546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(244436.09375, 13595.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(244409.109375, 13614.620117188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(244381.46875, 13632.627929688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(244347.234375, 13576.436523438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(244374.078125, 13558.54296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(244400.859375, 13541.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(244427.828125, 13522.731445312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(244455.453125, 13504.700195312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(244122.171875, 13836.908203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(244099.9375, 13804.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(244077.40625, 13772.088867188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(244049.421875, 13791.037109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(244093.15625, 13856.549804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(244071.125, 13824.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(243996.95209145, 14088.60620542, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(243812.94043058, 14147.065307922, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(243713.0821222, 14227.101688294, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=40.0, width=40.0, height=12.0, shelter=False))


class K1_Base(Airport):
    id = 11
    name = "K1 Base"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3800000, vhf_low_hz=38500000, vhf_high_hz=118000000, uhf_hz=250100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(250079.988298, 7392.006552, terrain), terrain)

        self.runways.append(Runway(id=None, name='32-14', main=RunwayApproach(name='32', heading=320, beacons=[]), opposite=RunwayApproach(name='14', heading=140, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(249772.453125, 7114.5122070312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(249732.609375, 7145.6381835938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(249692.515625, 7177.20703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(249652.296875, 7210.4643554688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(250378.78125, 7739.2431640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(250418.40625, 7707.8564453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(250458.296875, 7676.025390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(250498.296875, 7642.5053710938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(249611.0625, 7243.6274414062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(250539.59375, 7608.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(250277.328125, 6866.017578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(250242.328125, 6893.486328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(250207.265625, 6921.7197265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(250171.90625, 6949.8901367188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(250135.59375, 6979.1044921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(250099.078125, 7009.1010742188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(250742, 7290.892578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(250777.078125, 7262.689453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(250812.46875, 7234.548828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(250848.796875, 7205.365234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(250885.34375, 7175.3999023438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(250777.4375, 7137.1088867188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(250742.4375, 7164.5776367188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(250707.375, 7192.8110351562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(250672.015625, 7220.9814453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(250262.328125, 7005.4418945312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(250298.65625, 6976.2587890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(250226.9375, 7033.5825195312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(250191.859375, 7061.7861328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(250773.109375, 7466.8559570312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(250749.265625, 7486.876953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(250724.484375, 7506.9619140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(250698.40625, 7527.568359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(250672.328125, 7548.1743164062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(249984.375, 6931.7783203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='42', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(249961.234375, 6949.8603515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='43', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(249936.9375, 6968.7783203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='44', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(249913.78125, 6986.8603515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='45', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(249891.34375, 7005.2998046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='46', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(249868.078125, 7023.8818359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='47', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(250621.234375, 7423.2431640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(250637.75, 7446.1000976562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(250655.140625, 7468.0541992188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(250603.609375, 7402.9833984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(250541.96875, 7345.0092773438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(250515.859375, 7366.8676757812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(249961.84375, 7052.509765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(249979.671875, 7075.1430664062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(249997.921875, 7098.599609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(250015.75, 7121.2329101562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(250033.546875, 7143.1162109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))


class Al_Sahra_Airport(Airport):
    id = 12
    name = "Al-Sahra Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=118050000, uhf_hz=250150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(157133.335938, -61804.708984, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield12_0'))
        self.runways.append(Runway(id=1, name='14L-32R', main=RunwayApproach(name='14L', heading=140, beacons=[]), opposite=RunwayApproach(name='32R', heading=320, beacons=[])))
        self.runways.append(Runway(id=2, name='14R-32L', main=RunwayApproach(name='14R', heading=140, beacons=[]), opposite=RunwayApproach(name='32L', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(157650.375, -61074.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(157611.6875, -61044, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(157742.3125, -60420.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(157705.140625, -60392.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(157667.84375, -60364.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(157630.796875, -60336.66796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(157604.40625, -60230.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(157587.46875, -60254.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(157570.71875, -60276.04296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(157568.234375, -61012.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(157654.890625, -60899.81640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(157694.03125, -60929.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(157737.96875, -60959.63671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(156419.609375, -60830.42578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(156388.765625, -60807.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(156356.84375, -60786.80859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(158404.984375, -62317.68359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(158380.5, -62298.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(158354.671875, -62279.18359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(158328.328125, -62259.87890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(158302.59375, -62237.23046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(158507.140625, -62394.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(158482.65625, -62375.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(158456.84375, -62355.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(158430.5, -62336.36328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(158560.4375, -62435.48046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(158534.09375, -62416.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(156323.578125, -60764.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(156292.75, -60741.13671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(156260.8125, -60720.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(156229.65625, -60694.64453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(156198.8125, -60671.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(156166.890625, -60651.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(156133.640625, -60628.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(156102.796875, -60605.35546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(156070.859375, -60585.01171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(156039.09375, -60555.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(155924, -60465.1953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='62', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(155895.90625, -60444.72265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='63', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(155868.203125, -60424.43359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='64', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(155840.484375, -60404.1484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='65', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(155812.234375, -60384.0390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='66', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(155887.453125, -60541.50390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='67', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(155860.234375, -60521.31640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='68', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(155831.5625, -60500.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='69', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(155804.140625, -60480.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='70', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(155776.09375, -60460.30859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='71', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(157800.234375, -60302.73828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(157782.25, -60289.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(157765.015625, -60275.87109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(157747.03125, -60262.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(157729.140625, -60250.44140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(157711.15625, -60237.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(157645.59375, -60188.29296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(157627.609375, -60175.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(157610.375, -60161.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(157592.390625, -60148.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(157574.5, -60135.99609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(157556.515625, -60123.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(157539.3125, -60109.24609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(158951.6875, -61160.54296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(158933.890625, -61147.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(158914.25, -61132.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(158896.46875, -61119.66796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(158783.703125, -61063.94921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(158760.71875, -61046.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(158736.984375, -61028.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(158878.5, -61106.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(158860.703125, -61093.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(158841.0625, -61078.65234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(158823.28125, -61065.46484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(158458.234375, -63255.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(158374.96875, -63173.94921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(158317.328125, -63270.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(158235.59375, -63193.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(156237.90625, -61694.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(156195.796875, -61664.80078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(156154.59375, -61635.06640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(156112.59375, -61603.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(156071.125, -61571.16015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(156030.171875, -61540.37890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(155986.34375, -61507.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(155944.875, -61475.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(155899.75, -61441.51953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(155856.703125, -61409.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(155832.6875, -61328.87890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=26.0, width=24.0, height=11.0, shelter=False))


class Al_Taquddum_Airport(Airport):
    id = 13
    name = "Al-Taquddum Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=135700000, uhf_hz=250200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(9716.665039, -58133.308594, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield13_0'))
        self.runways.append(Runway(id=1, name='12R-30', main=RunwayApproach(name='12R', heading=120, beacons=[]), opposite=RunwayApproach(name='30', heading=300, beacons=[])))
        self.runways.append(Runway(id=1, name='12L-30R', main=RunwayApproach(name='12L', heading=120, beacons=[]), opposite=RunwayApproach(name='30R', heading=300, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(8219.69140625, -57364.42578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(8153.5522460938, -57401.15234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(8086.7641601562, -57442.17578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(10912.2734375, -59522.26953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(10898.934570312, -59796.16796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(10215.733398438, -57812.98828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(10203.530273438, -57793.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(10255.934570312, -57853.91015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(10273.442382812, -57884.56640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(10290.243164062, -57913.97265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(10307.198242188, -57942.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(9991.4208984375, -58068.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(10019.625976562, -58050.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(10047.013671875, -58034.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(10075.184570312, -58018.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(10104.137695312, -58001.56640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(10132.30859375, -57985.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(10160.479492188, -57967.91796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(10196.997070312, -57962.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(10225.16796875, -57944.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(10191.091796875, -57773.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(10179.298828125, -57752.50390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(10167.59375, -57732.84765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(10155.80078125, -57712.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(10143.396484375, -57691.96484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(10131.25390625, -57669.77734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(10120.684570312, -57650.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(10107.755859375, -57630.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(10095.788085938, -57609.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(10084.431640625, -57588.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(10071.901367188, -57568.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(10060.580078125, -57548.31640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(10153.71875, -57849.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(10142.500976562, -57829.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(10129.908203125, -57808.87890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(10117.96875, -57787.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(10106.61328125, -57768.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(10094.237304688, -57748.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(10082.153320312, -57727.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(10069.341796875, -57705.87109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(10057.985351562, -57686.65234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(10045.974609375, -57666.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(10034.399414062, -57645.23046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(10022.315429688, -57624.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(10010.741210938, -57604.17578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(9998.583984375, -57583.57421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(8080.138671875, -56640.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(10260.12890625, -60603.76171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(10135.34765625, -60358.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(10069.859375, -60162.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(9095.73046875, -59437.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(9069.0390625, -59453.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(9042.623046875, -59469.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(9015.150390625, -59485.16015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(8758.1123046875, -59481.27734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(8323.7392578125, -58245.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(8337.103515625, -58053.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(8307.7587890625, -58384.31640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(8156.4770507812, -57911.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(7964.5615234375, -57895.23046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(7651.5732421875, -57778.44921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(7581.8564453125, -57926.03515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(7404.6533203125, -58160.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(10546.350808735, -59862.611106175, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(10472.468008358, -59872.101463479, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(10872.456054688, -59657.08203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(10891.953125, -59584.23828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(10808.047851562, -59341.12109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(10766.172851562, -59267.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(9447.9384765625, -57207.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(8920.4990234375, -56159.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(6937.6235351562, -56808.36328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(6969.8564453125, -56813.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(7002.6787109375, -56817.30078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(7035.5102539062, -56821.75390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(7068.3330078125, -56825.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(7101.1552734375, -56830.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(7133.9775390625, -56834.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(7166.318359375, -56839.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(7199.140625, -56843.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(7231.8364257812, -56848.07421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(7264.6586914062, -56852.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(7298.5903320312, -56857.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(7331.4125976562, -56861.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))


class Al_Salam_Airbase(Airport):
    id = 14
    name = "Al-Salam Airbase"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=38650000, vhf_high_hz=118100000, uhf_hz=250250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(2262.854797, 25199.399414, terrain), terrain)

        self.runways.append(Runway(id=None, name='15-33', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33', heading=330, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(3264.9204101562, 24226.220703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(3375.5224609375, 24277.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(2673.4951171875, 25503.33203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(2613.9094238281, 25540.986328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(2311.4343261719, 25878.23828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(3196.6218261719, 24196.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(3163.6538085938, 24162.98046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(3130.8315429688, 24129.505859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(3083.2280273438, 24109.724609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(3062.1457519531, 24087.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(3040.6264648438, 24066.037109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(3018.8896484375, 24043.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(2997.1530761719, 24021.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(2975.8510742188, 23998.435546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(2954.3315429688, 23975.830078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(2931.5080566406, 23952.572265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(2908.6845703125, 23928.443359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(2885.4262695312, 23905.185546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(2862.16796875, 23881.05859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(2839.3444824219, 23858.017578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(2820.0119628906, 23831.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(2775.9953613281, 23820.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(2756.5959472656, 23834.15234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(2738.6330566406, 23846.83203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(2721.4248046875, 23859.361328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(2733.6994628906, 23909.884765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(2830.9309082031, 24016.232421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(2813.3505859375, 23993.14453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(2795.091796875, 23968.58203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(2785.7473144531, 23935.759765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(2771.8359375, 23916.197265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(3319.4677734375, 24258.119140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(3424.953125, 24345.955078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(3444.3764648438, 24374.755859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(3466.1218261719, 24413.19140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(3376.8481445312, 24646.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(3394.8422851562, 24603.416015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(3413.6228027344, 24559.85546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(3434.5422363281, 24529.115234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(3444.9758300781, 24502.814453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(3359.1926269531, 24689.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(3342.1655273438, 24725.623046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(3330.1022949219, 24754.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(3317.4226074219, 24782.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(3305.6486816406, 24811.205078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(3293.3310546875, 24840.912109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(3281.3759765625, 24870.076171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(3268.8774414062, 24898.876953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(3256.1975097656, 24927.49609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(3243.1555175781, 24956.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(3230.81640625, 24987.11328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(3216.9482421875, 25015.197265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(3203.6889648438, 25043.455078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(3191.0815429688, 25072.36328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(3177.822265625, 25101.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(3162.7978515625, 25130.96484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(3148.0788574219, 25159.166015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(3134.1311035156, 25186.158203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(3118.9155273438, 25212.603515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(3104.60546875, 25240.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(3089.7521972656, 25268.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(2236.1936035156, 25893.041015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='97', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(2246.6025390625, 25852.05078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='96', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(2256.5944824219, 25811.26953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='95', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(2267.5205078125, 25769.171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='94', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(2132.6413574219, 25869.57421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='101', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(2142.9006347656, 25828.861328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='100', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(2153.5778808594, 25787.939453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='99', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(2412.8686523438, 25769.568359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='92', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(2156.5563964844, 25751.865234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='98', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(2492.4223632812, 25455.734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='76', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(2509.1442871094, 25480.5234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='77', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(2525.5556640625, 25506.041015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='78', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(2409.6962890625, 25481.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='79', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(2432.8862304688, 25517.1171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='80', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(2455.9926757812, 25552.830078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='81', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(2370.7080078125, 25508.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='82', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(2393.3134765625, 25545.001953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='83', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(2416.0065917969, 25580.736328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='84', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(2475.2473144531, 25430.6953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='75', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(2324.0480957031, 25603.814453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='87', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(2308.0893554688, 25578.529296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='86', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(2292.4633789062, 25552.521484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='85', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(2340.4521484375, 25629.3671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='88', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(2223.2106933594, 25594.5703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='89', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(2238.8364257812, 25620.576171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='90', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(2254.7954101562, 25645.86328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='91', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(2683.693359375, 25393.154296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(2720.404296875, 25368.998046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(2756.4001464844, 25344.896484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(2791.7702636719, 25321.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(2829.9572753906, 25297.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(2867.2053222656, 25273.529296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(2901.3232421875, 25249.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(2937.6323242188, 25227.205078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(2959.4521484375, 25275.548828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(2972.19140625, 25250.75390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(2997.3146972656, 25202.416015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(2984.5754394531, 25227.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(3022.8913574219, 25152.236328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(3009.8913574219, 25177.29296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=11.0, shelter=False))


ALL_AIRPORTS: List[Type[Airport]] = [
    Al_Asad_Airbase,
    Baghdad_International_Airport,
    Erbil_International_Airport,
    Bashur_Airport,
    Qayyarah_Airfield_West,
    Sulaimaniyah_International_Airport,
    Balad_Airbase,
    Al_Taji_Airport,
    Kirkuk_International_Airport,
    K1_Base,
    Al_Sahra_Airport,
    Al_Taquddum_Airport,
    Al_Salam_Airbase,
]

