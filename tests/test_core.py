import os
import unittest
import openpipe
from openpipe.core import Project, get_project_name, get_shot_info, say_hello


class TestCore(unittest.TestCase):
    def test_version(self):
        self.assertEqual(openpipe.__version__, "0.0.1")

    def test_project_helpers(self):
        self.assertEqual(get_project_name(), "OpenPipe")
        self.assertEqual(say_hello(), "Hello from OpenPipe core!")

    def test_project_class(self):
        prj = Project("Demo_Show", "D:/Dev/Projects")
        self.assertEqual(prj.name, "Demo_Show")
        self.assertEqual(prj.get_project_dir(), os.path.normpath("D:/Dev/Projects"))

    def test_get_shot_info(self):
        sample_path = "D:/Dev/Projects/OpenPipe/shot_AS_010_v005.nk"
        info = get_shot_info(sample_path)
        self.assertEqual(info, {"shot": "shot_AS_010", "version": 5})
        self.assertIsNone(get_shot_info("invalid_filename.nk"))


if __name__ == "__main__":
    unittest.main()

