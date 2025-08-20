from os.path import abspath, join, exists, dirname, isdir
from os import makedirs


def write_file(working_directory, file_path, content):
    abs_workdir = abspath(working_directory)
    abs_file_path = abspath(join(working_directory, file_path))

    if not abs_file_path.startswith(abs_workdir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not exists(abs_file_path):
        try:
            makedirs(dirname(abs_file_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if exists(abs_file_path) and isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'

    try:
        with open(abs_file_path, "w") as file:
            file.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error writing to file: {e}"
