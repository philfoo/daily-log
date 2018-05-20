import os.path
import consts

def run(input_arr):
    # clean up input data
    if (len(input_arr) <= 1):
        print consts.MISSING_ARGUMENTS
        return

    search_string = input_arr[1]

    file_array = os.listdir(consts.DIR_LOC)
    print file_array
