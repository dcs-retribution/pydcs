import json
import os
import unittest
import zipfile

import dcs
from dcs import mapping
from dcs.planes import FA_18C_hornet, F_14B


class DtcCartridgeTests(unittest.TestCase):
    """Native DTC data cartridges: DTC/<name>.dtc files in the miz + the
    per-unit DTC.Cartridges/AutoLoad block."""

    def setUp(self):
        os.makedirs('missions', exist_ok=True)

    def _mission_with_hornets(self):
        m = dcs.mission.Mission()
        usa = m.country("USA")
        fg = m.flight_group_inflight(
            usa,
            "DTC Group",
            FA_18C_hornet,
            mapping.Point(-250000, 600000, m.terrain),
            6000,
            group_size=2,
        )
        return m, fg

    def test_save_writes_cartridge_file_and_unit_block(self):
        m, fg = self._mission_with_hornets()
        cartridge = json.dumps(
            {"data": {"COMM": {}}, "name": "Test Cartridge", "type": "FA-18C_hornet"}
        )
        m.add_dtc_cartridge("Test Cartridge", cartridge)
        fg.units[0].add_dtc_cartridge("Test Cartridge")

        lead = fg.units[0].dict()
        self.assertEqual(
            lead["DTC"],
            {
                "Cartridges": {1: {"default": True, "name": "Test Cartridge"}},
                "AutoLoad": True,
            },
        )
        self.assertNotIn("DTC", fg.units[1].dict())

        path = 'missions/dtc_test.miz'
        m.save(path)
        with zipfile.ZipFile(path) as miz:
            self.assertIn('DTC/Test Cartridge.dtc', miz.namelist())
            self.assertEqual(
                json.loads(miz.read('DTC/Test Cartridge.dtc'))["name"],
                "Test Cartridge",
            )
            mission_text = miz.read('mission').decode('utf-8')
            self.assertIn('"AutoLoad"', mission_text)
            self.assertIn('"Test Cartridge"', mission_text)

    def test_cartridges_round_trip_through_load_and_save(self):
        m, fg = self._mission_with_hornets()
        m.add_dtc_cartridge("Round Trip", '{"data": {}, "name": "Round Trip"}')
        fg.units[0].add_dtc_cartridge("Round Trip")
        path = 'missions/dtc_round_trip.miz'
        m.save(path)

        m2 = dcs.mission.Mission()
        m2.load_file(path)
        self.assertEqual(
            m2.dtc_cartridges, {"Round Trip": '{"data": {}, "name": "Round Trip"}'}
        )
        unit = m2.country("USA").plane_group[0].units[0]
        self.assertEqual(
            unit.dtc_cartridges, [{"name": "Round Trip", "default": True}]
        )
        self.assertTrue(unit.dtc_autoload)

        path2 = 'missions/dtc_round_trip2.miz'
        m2.save(path2)
        with zipfile.ZipFile(path2) as miz:
            self.assertIn('DTC/Round Trip.dtc', miz.namelist())
            # The reserved-files handling must not duplicate the entry via the
            # binary-resource pass.
            self.assertEqual(
                [n for n in miz.namelist() if n.startswith('DTC/')],
                ['DTC/Round Trip.dtc'],
            )
            self.assertIn('"AutoLoad"', miz.read('mission').decode('utf-8'))

    def test_missions_without_cartridges_are_unchanged(self):
        m, fg = self._mission_with_hornets()
        self.assertNotIn("DTC", fg.units[0].dict())
        path = 'missions/dtc_none.miz'
        m.save(path)
        with zipfile.ZipFile(path) as miz:
            self.assertEqual(
                [n for n in miz.namelist() if n.startswith('DTC/')], []
            )

    def test_cartridge_works_for_any_airframe_eg_tomcat(self):
        # The DTC API is airframe-agnostic: it is not special-cased to the
        # FA-18C/F-16C. Any DTC-capable module (e.g. the F-14B / F-14B(U),
        # which DCS 2.9.28 gave native DTC support) uses the exact same path.
        m = dcs.mission.Mission()
        usa = m.country("USA")
        fg = m.flight_group_inflight(
            usa,
            "Tomcat DTC",
            F_14B,
            mapping.Point(-250000, 600000, m.terrain),
            6000,
            group_size=2,
        )
        m.add_dtc_cartridge("Tomcat Cartridge", '{"data": {}, "name": "Tomcat Cartridge"}')
        fg.units[0].add_dtc_cartridge("Tomcat Cartridge")

        lead = fg.units[0].dict()
        self.assertEqual(
            lead["DTC"],
            {
                "Cartridges": {1: {"default": True, "name": "Tomcat Cartridge"}},
                "AutoLoad": True,
            },
        )

        path = 'missions/dtc_tomcat.miz'
        m.save(path)
        m2 = dcs.mission.Mission()
        m2.load_file(path)
        self.assertIn("Tomcat Cartridge", m2.dtc_cartridges)
        unit = m2.country("USA").plane_group[0].units[0]
        self.assertEqual(unit.dtc_cartridges, [{"name": "Tomcat Cartridge", "default": True}])
        self.assertTrue(unit.dtc_autoload)


if __name__ == '__main__':
    unittest.main()
