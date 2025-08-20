from os.path import abspath, join, exists, dirname, isdir
from os import makedirs


def write_file(working_directory, file_path, content):
    abs_workdir = abspath(working_directory)
    target_file = abspath(join(working_directory, file_path))

    if not target_file.startswith(abs_workdir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    create_dir = dirname(abspath(file_path))
    if not exists(create_dir):
        try:
            makedirs(create_dir, exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if exists(create_dir) and isdir(create_dir):
        return f'Error: "{file_path}" is a directory, not a file'

    try:
        with open(target_file, "w") as file:
            file.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error writing to file: {e}"
