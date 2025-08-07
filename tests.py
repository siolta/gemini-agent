import unittest

from functions.get_files_info import get_files_info


class TestGetFiles(unittest.TestCase):
    # def tests here
    def test_same_dir(self):
        result = """- tests.py: file_size: 1343 bytes, is_dir=False
- main.py: file_size: 576 bytes, is_dir=False
- pkg: file_size: 128 bytes, is_dir=True
"""
        print(get_files_info("calculator", "."))
        self.assertEqual(get_files_info("calculator", "."), result)

    def test_inside_work_dir(self):
        result = """- render.py: file_size: 768 bytes, is_dir=False
- calculator.py: file_size: 1739 bytes, is_dir=False
"""
        print(get_files_info("calculator", "pkg"))
        self.assertEqual(get_files_info("calculator", "pkg"), result)

    def test_outside_work_dir(self):
        result = (
            'Error: Cannot list "/bin" as it is outside the permitted working directory'
        )
        print(get_files_info("calculator", "/bin"))
        self.assertEqual(get_files_info("calculator", "/bin"), result)

    def test_relative_outside_work_dir(self):
        result = (
            'Error: Cannot list "../" as it is outside the permitted working directory'
        )
        print(get_files_info("calculator", "../"))
        self.assertEqual(get_files_info("calculator", "../"), result)


if __name__ == "__main__":
    unittest.main()
