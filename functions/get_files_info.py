from os.path import abspath, isdir, join
from os import listdir


def get_files_info(working_directory, directory=None):
    #

    dir_str = abspath(directory)
    workdir_str = abspath(working_directory)

    if not isdir(directory):
        return f'Error: "{directory}" is not a directory'

    if not dir_str.startswith(workdir_str):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # get list of files and make a string
    # directory might be a sub_dir of working_dir
    # file_name, file_size, is_dir
    # use os.listdir to get files, then build dict of info?
    # os.path.getsize() | os.path.isfile()

    files = listdir(directory)
    output = []

    for file in files:
        f_path = join(directory, file)
        output.append("f- {file}: file_size: {getsize(f_path)}, is_dir={isdir(f_path)}")

    return output
