from os.path import abspath, join, exists
from subprocess import run

from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    abs_workdir = abspath(working_directory)
    abs_file_path = abspath(join(working_directory, file_path))

    if not abs_file_path.startswith(abs_workdir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        commands = ["python3", abs_file_path]
        if args:
            commands.extend(args)

        completed_process = run(commands, capture_output=True, text=True, timeout=30, cwd=abs_workdir)

        output = []
        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stdout:
            output.append(f"STDERR:\n{completed_process.stderr}")

        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")

        return "\n".join(output) if output else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file contents of a file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the target python file to run, relative to the working directory. Required in order to get successful output.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="A list of optional args to supply to the python script at run declaration.",
            ),
        },
    ),
)
