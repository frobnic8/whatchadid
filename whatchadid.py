#!/usr/bin/env python

"""whatchadid.py - turn the WhatchaDoingLog.XML into an CSV file, since the
built in export to CSV (or XLS) functionality doesn't really work.
"""

import bs4
import sys
from os.path import expanduser, join
from logging import debug, warning

__author__ = 'erskin@eldritch.org'
__version__ = "0.5.1"

# The delimiter used to separate columns in the output.
# TODO: Add argument options to allow the use tabs instead of commas.
DELIMITER = ','

# A dictionary of raw task name to pretty task name.
COL_NAMES = {
    'task': 'Task',
    'starttime': 'Started',
    'submittime': 'Submitted',
    'endtime': 'Ended',
    'elapsedseconds': 'Seconds',
    'elapsedminutes': 'Minutes',
    'elapsedhours': 'Hours',
}


def parse_datetime(raw_value):
    """Convert the WhatchaDoing date time string into something
    spreadsheet friendly.

    e.g. 2013-06-07T18:10:14.000Z into 2013-06-07 18:10:14

    """
    debug('Parsing raw datetime value: ' + repr(raw_value))
    if raw_value:
        try:
            return raw_value[:10] + ' ' + raw_value[11:19]
        except:
            warning('Could not parse datetime: ' + raw_value)
            return raw_value
    else:
        return ''


def double_quote(raw_string):
    """Quote the column in double quotes to contain any potential commas."""
    return '"%s"' % (raw_string)

# A dictionary of raw task name to optional parsing functions.
COL_PARSERS = {
    'task': double_quote,
    'starttime': parse_datetime,
    'submittime': parse_datetime,
    'endtime': parse_datetime,
}

# Column output order.
COL_ORDER = ['task', 'starttime', 'submittime', 'endtime', 'elapsedseconds',
             'elapsedminutes', 'elapsedhours']

def main():
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
        logfile = open(join(expanduser('~'), 'Documents', 'WhatchaDoingLog.XML'))

    # Parse the log file.
    activities = bs4.BeautifulSoup(logfile).find_all('activity')

    # Create a header row
    print DELIMITER.join(['"%s"' % (COL_NAMES[col]) for col in COL_ORDER])

    # Create a row from each activity record.
    for activity in activities:
        row = []
        for col in COL_ORDER:
            raw_value = activity.find(col).text
            if col in COL_PARSERS:
                raw_value = COL_PARSERS[col](raw_value)
            row.append(raw_value)
        print DELIMITER.join(row)

if __name__ == '__main__':
    main()
