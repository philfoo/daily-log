import re
import consts as consts
import os.path

import reader as reader
import writer as writer
import searcher as searcher

def main():
    # Check whether stuff has been set up already
    if (not os.path.exists(consts.DIR_LOC)):
        print consts.SETUP_LOG_TEXT

        os.makedirs(consts.DIR_LOC)

    while (True):
        user_input= raw_input(consts.COMMAND_TEXT)
        user_input_array = user_input.split()

        if (len(user_input_array) > 0):
            command = user_input_array[0].lower()

            if (command in consts.HELP):
                print consts.HELP_MESSAGE

            elif (command in consts.WRITE):
                writer.run(user_input_array)

            elif (command in consts.READ):
                reader.run(user_input_array)

            elif (command in consts.SEARCH):
                searcher.run(user_input_array)

            elif (command in consts.DELETE):
                print "Deleting"

            elif (command in consts.EDIT):
                writer.run(user_input_array)

            elif (command in consts.QUIT):
                break

            else:
                print consts.UNRECOGNIZED_COMMAND_TEXT

if __name__ == '__main__':
    main()
