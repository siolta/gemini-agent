from os.path import abspath, join, exists
from subprocess import run


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

        completed_process = run(
            commands, capture_output=True, text=True, timeout=30, cwd=abs_workdir
        )

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
