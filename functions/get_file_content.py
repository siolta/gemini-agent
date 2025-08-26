from os.path import abspath, join, isfile
from google.genai import types
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    abs_workdir = abspath(working_directory)
    target_file = abspath(join(working_directory, file_path))

    if not target_file.startswith(abs_workdir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(target_file, "r") as file:
            file_content_str = file.read(MAX_CHARS)
            if len(file_content_str) == MAX_CHARS:
                file_content_str += f'[...File "{file_path}" truncated at "{MAX_CHARS}" characters]'
        return file_content_str

    except Exception as e:
        return f"Error reading file: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {
        MAX_CHARS
    } characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
