from datetime import datetime
from subprocess import call
import tempfile, os

import consts

def run(input_arr):
    # Clean up input data
    if (len(input_arr) <= 1):
        print consts.MISSING_ARGUMENTS
        return

    if (input_arr[1].lower() == "today"):
        date =  datetime.now()
    else:
        try:
            date = datetime.strptime(input_arr[1], '%m/%d/%Y')
        except ValueError as val_error:
            print val_error
            return

    file_name = ('%02d' % date.month) + ('%02d' % date.day) + ('%02d' % date.year) + ".txt"
    write_file(file_name)

def write_file(file_name):
    file_path = consts.DIR_LOC + file_name
    initial_contents = ""

    if (os.path.exists(file_path)):
        file_object = open(file_path, 'r')
        initial_contents += file_object.read()
        file_object.close()

    # Create new file, write to it
    EDITOR = os.environ.get('EDITOR', 'vim')

    with tempfile.NamedTemporaryFile(suffix='.tmp') as tf:
        tf.write(initial_contents)
        tf.flush()
        call([EDITOR, tf.name])

        tf.seek(0)
        finished_contents = tf.read()

    file_object = open(file_path, 'w')
    file_object.write(finished_contents)
    file_object.close()

    # Delete file if there are no contents
    if (len(finished_contents) == 0):
        os.unlink(file_path)



