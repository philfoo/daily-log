from datetime import datetime, timedelta
import consts

def run(input_arr):
    # Clean up input data
    if (len(input_arr) <= 1):
        print consts.MISSING_ARGUMENTS
        return

    # TODO: Try for date formatted in MM/DD/YYYY, else try MM/DD/YY
    try:
        date = datetime.strptime(input_arr[1], '%m/%d/%Y')
    except ValueError as val_error:
        print val_error
        return

    if (len(input_arr) == 2):
        find_necessary_dates(date, 0)
    else:
        days_after = int(input_arr[2])
        find_necessary_dates(date, days_after)

# Takes a datetime object, and X number of days
# Returns an array with the initial date and the
# X days after the initial date.
# Expected format of date: MM/DD/YYYY
def find_necessary_dates(date, days_after):
    days_counted = 0
    necessary_dates = []

    necessary_dates.append(date)
    while (days_counted != days_after):
        date += timedelta(days=1)
        necessary_dates.append(date)
        days_counted += 1

    print convert_dates_to_filenames(necessary_dates)
    return necessary_dates

# Takes an array of datetime objects and returns a string
# in format 'MMDDYYYY.txt''
def convert_dates_to_filenames(dates_array):
    file_names = []
    for date in dates_array:
        file_name = ('%02d' % date.month) + ('%02d' % date.day) + ('%02d' % date.year) + ".txt"
        file_names.append(file_name)

    return file_names

