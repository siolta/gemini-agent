from os.path import abspath, join, exists, dirname, isdir
from os import makedirs

from google.genai import types


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
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error writing to file: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the passed input to the target file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the target file, relative to the working directory. Required in order to get successful output.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the target file.",
            ),
        },
    ),
)
