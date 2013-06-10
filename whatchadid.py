#!/usr/bin/env python

"""whatchadid.py - turn the WhatchaDoingLog.XML into an CSV file, since the
built in export to CSV (or XLS) functionality doesn't really work.
"""

import bs4
import sys
from os.path import expanduser, join

# The delimiter used to separate columns in the output.
# TODO: Add argument options to allow the use tabs instead of commas.
DELIMITER = ','

# A dictionary of raw task name to pretty task name.
# NOTE: We use a dirty hack to split some columns in two here.
COL_NAMES = {
    'task': 'Task',
    'starttime': DELIMITER.join(['Start Date', 'Start Time']),
    'submittime': DELIMITER.join(['Submit Date', 'Submit Time']),
    'endtime': DELIMITER.join(['End Date', 'End Time']),
    'elapsedseconds': 'Seconds',
    'elapsedminutes': 'Minutes',
    'elapsedhours': 'Hours',
}


# NOTE: We use a dirty hack to split some columns in two here.
def split_datetime(datetime_string):
    """Convert the WhatchaDoing date time string into two columns.
    e.g. 2013-06-07T18:10:14.000Z

    """
    return DELIMITER.join([datetime_string[0:10], datetime_string[11:19]])

# A dictionary of raw task name to optional parsing functions.
# NOTE: We use a dirty hack to split some columns in two here.
COL_PARSERS = {
    'starttime': split_datetime,
    'submittime': split_datetime,
    'endtime': split_datetime,
}

# Column output order.
COL_ORDER = ['task', 'starttime', 'submittime', 'endtime', 'elapsedseconds',
             'elapsedminutes', 'elapsedhours']

# Use the default file location
if len(sys.argv) > 1:
    if sys.argv[1].lower() in ('-h', '--help', '-?'):
        print 'Create an actual CSV file from a WhatchaDoingLog.XML file'
        print 'usage: %s [log_file]'
        sys.exit()
    if sys.argv[1] == '-':
        logfile = sys.stdin
    else:
        logfile = open(sys.argv[1])
else:
    logfile = open(join(expanduser('~'), 'WhatchaDoingLog.XML'))

# Parse the log file.
activities = bs4.BeautifulSoup(logfile).find_all('activity')

# Create a header row
print DELIMITER.join([COL_NAMES[col] for col in COL_ORDER])

# Create a row from each activity record.
for activity in activities:
    row = []
    for col in COL_ORDER:
        raw_value = activity.find(col).text
        if col in COL_PARSERS:
            raw_value = COL_PARSERS[col](raw_value)
        row.append(raw_value)
    print DELIMITER.join(row)
