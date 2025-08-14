import unittest

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


class TestGetFiles(unittest.TestCase):
    # def tests here
    def test_same_dir(self):
        result = """- lorem.txt: file_size: 67855 bytes, is_dir=False
- tests.py: file_size: 1343 bytes, is_dir=False
- main.py: file_size: 576 bytes, is_dir=False
- pkg: file_size: 128 bytes, is_dir=True"""
        print("Result for current directory:")
        print(get_files_info("calculator", "."))
        print("")
        self.assertEqual(get_files_info("calculator", "."), result)

    def test_inside_work_dir(self):
        result = """- render.py: file_size: 768 bytes, is_dir=False
- calculator.py: file_size: 1739 bytes, is_dir=False"""
        print("Result for 'pkg' directory:")
        print(get_files_info("calculator", "pkg"))
        print("")
        self.assertEqual(get_files_info("calculator", "pkg"), result)

    def test_outside_work_dir(self):
        result = (
            'Error: Cannot list "/bin" as it is outside the permitted working directory'
        )
        print("Result for '/bin' directory:")
        print(get_files_info("calculator", "/bin"))
        print("")
        self.assertEqual(get_files_info("calculator", "/bin"), result)

    def test_relative_outside_work_dir(self):
        result = (
            'Error: Cannot list "../" as it is outside the permitted working directory'
        )
        print("Result for '../' directory:")
        print(get_files_info("calculator", "../"))
        print("")
        self.assertEqual(get_files_info("calculator", "../"), result)


class TestGetFileContent(unittest.TestCase):
    def test_file_in_work_dir(self):
        func = get_file_content("calculator", "main.py")
        result = "def main()"
        print("Result for 'main.py' file:")
        print(func[:100])
        print("")
        self.assertIn(result, func)

    def test_file_in_sub_work_dir(self):
        func = get_file_content("calculator", "pkg/calculator.py")
        result = "def _apply_operator(self, operators, values)"
        print("Result for 'pkg/calculator.py' file:")
        print(func[:100])
        print("")
        self.assertIn(result, func)

    def test_file_outside_work_dir(self):
        # (this should return an error string)
        func = get_file_content("calculator", "/bin/cat")
        result = 'Error: Cannot read "/bin/cat" as it is outside the permitted working directory'
        print("Result for '/bin/cat' file:")
        print(func)
        print("")
        self.assertIn(result, func)

    def test_file_does_not_exist(self):
        # (this should return an error string)
        func = get_file_content("calculator", "pkg/does_not_exist.py")
        result = (
            'Error: File not found or is not a regular file: "pkg/does_not_exist.py"'
        )
        print("Result for 'pkg/does_not_exist.py' file:")
        print(func)
        print("")
        self.assertIn(result, func)


if __name__ == "__main__":
    unittest.main()
