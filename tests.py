import unittest

from functions.get_files_info import get_files_info


class TestGetFiles(unittest.TestCase):
    # def tests here
    def test_same_dir(self):
        self.assertEqual(
            get_files_info("calculator", "./calculator"),
            """Result for current directory:
 - main.py: file_size=576 bytes, is_dir=False
 - tests.py: file_size=1343 bytes, is_dir=False
 - pkg: file_size=92 bytes, is_dir=True
 - lorem.txt: file_size=28 bytes, is_dir=False""",
        )

    def test_outside_work_dir(self):
        # 'Error: Cannot list "./" as it is outside the permitted working directory',
        pass


if __name__ == "__main__":
    unittest.main()
