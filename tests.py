import unittest

from functions.run_python import run_python_file
from main import generate_content


class TestOutput(unittest.TestCase):
    def test(self):
        result = run_python_file("calculator", "main.py")
        print(result)

        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)

        result = run_python_file("./calculator", "tests.py")
        print(result)

        result = run_python_file("calculator", "../main.py")
        print(result)

        result = run_python_file("calculator", "nonexistent.py")
        print(result)


if __name__ == "__main__":
    unittest.main()
