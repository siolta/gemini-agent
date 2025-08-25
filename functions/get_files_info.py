from os.path import abspath, isdir, join, getsize
from os import listdir
from google.genai import types


def get_files_info(working_directory, directory="."):
    abs_workdir = abspath(working_directory)
    target_dir = abspath(join(working_directory, directory))

    if not target_dir.startswith(abs_workdir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        files = listdir(target_dir)
        file_info = []

        for file in files:
            f_path = join(target_dir, file)
            file_info.append(f"- {file}: file_size: {getsize(f_path)} bytes, is_dir={isdir(f_path)}")

        return "\n".join(file_info)

    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
