from os.path import abspath, join, isfile


def get_file_content(working_directory, file_path):
    abs_workdir = abspath(working_directory)
    target_dir = abspath(join(working_directory, file_path))

    if not target_dir.startswith(abs_workdir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    pass

