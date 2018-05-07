import re
import consts as consts

# TODO:Check whether stuff has been set up first (the actual daily log)


while (True):
    user_input= raw_input(consts.COMMAND_TEXT)
    user_input_array = user_input.split()

    if (len(user_input_array) > 0):
        command = user_input_array[0].lower()

        if (command in consts.HELP):
            print consts.HELP_MESSAGE

        if (command in consts.WRITE):
            print "Writing"

        if (command in consts.FIND):
            print "Finding"

        if (command in consts.SEARCH):
            print "Searching"

        if (command in consts.DELETE):
            print "Deleting"

        if (command in consts.EDIT):
            print "Editing"

        if (command in consts.QUIT):
            break


