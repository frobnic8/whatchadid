whatchadid
==========

Parse a WhatchDoingLog.XML into a CSV file to standard out.

The default export as CSV or XLS from WhatchaDoing is broken. This processes
the log file using BeautifulSoup 4 to produce a CSV.

Local installation
------------------

The whatchadid tool is now available in a nice egg package.

If you've never installed python stuff before, this will probably be the
terminal commands you want to run: (This will prompt you for your login
password)

    sudo easy_install pip
    sudo pip install --upgrade setuptools
    sudo pip install git+https://github.va.opower.it/erskin-cherry/whatchadid

To test your installation, run:

    whatchadid --help

If you are still having problems, just let Erskin know and he'll help you out.

Usage
-----
Example usage:

    ./whatchadid > raw_whatchadoing_data.csv

whatchadid.py takes the "-h" or "--help" option to display minimal usage.

If run with no arguments, it looks in the "Documents" folder of your home
directory. If the given a single argument, it reads that as the log file
instead. If the argument is "-", it reads from standard input.

You can optionall change the DELIMITER constant in the code if you need a
different delimiter.

Currently, it does not support filtering and parses the entire log.
