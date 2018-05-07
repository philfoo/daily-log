from datetime import datetime, timedelta

def run(input_arr):
    # Clean up input data
    assert(len(input_arr) > 1)

    date = datetime.strptime(input_arr[1], '%m/%d/%Y')
    if (len(input_arr) == 2):
        find_file_with_date(date, 0)
    else:
        days_after = int(input_arr[2])
        find_file_with_date(date, days_after)

# Expected format of date: MM/DD/YYYY
def find_file_with_date(date, days_after):
    days_counted = 0
    print date
    print days_after

    # while (days_counted != days_after):



