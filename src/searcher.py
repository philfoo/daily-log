import os.path
import re

import consts
import reader as reader

def run(input_arr):
    # clean up input data
    if (len(input_arr) <= 1):
        print consts.MISSING_ARGUMENTS
        return

    # TODO: Multiple search strings??
    search_string = input_arr[1]

    file_array = os.listdir(consts.DIR_LOC)
    files_with_text = []
    for file_name in file_array:
        if re.match(consts.FILE_REGEX, file_name):
            full_file_path = consts.DIR_LOC + file_name

            if (file_contains_text(full_file_path, search_string)):
                files_with_text.append(file_name)

    if (len(files_with_text) == 0):
        print consts.NO_MATCHES_TEXT
        return

    print reader.read_and_build_entries(files_with_text)

def file_contains_text(file_name, search_string):
    f = open(file_name, 'r')
    file_content = f.read()
    f.close()

    # Standardize cases
    file_content = file_content.lower()
    search_string = search_string.lower()

    return (search_string in file_content)


