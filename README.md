whatchadid
==========

Parse a WhatchDoingLog.XML into a CSV file to standard out.

The time tracking tool WhatchaDoing sucks, but it sucks less than its peers.
The default export as CSV or XLS from WhatchaDoing is broken. This tool
processes the raw WhatchaDoing log file (using BeautifulSoup 4) to produce a
working CSV you can load into a spreadsheet program.

You can find the WhatchaDoing time tracking software here:

    http://www.fish-bytes.com/whatchadoing/

Local installation
------------------

The whatchadid tool is now available in a nice wheel package.

If that doesn't mean anything to you and you've never installed python
stuff before, these will probably be the terminal commands you want to run:

    easy_install pip
    pip install --upgrade setuptools
    pip install git+https://github.com/frobnic8/whatchadid

If those fail, and this is your personal computer, you can try it again
with a little more poweful permissions: (This will prompt you for your login password)

    sudo easy_install pip
    sudo pip install --upgrade setuptools
    sudo pip install git+https://github.com/frobnic8/whatchadid

To test your installation, run:

    whatchadid --help

If you are still having problems, just let Erskin know and he'll help you out.

Usage
-----
Example usage:

    whatchadid > raw_whatchadoing_data.csv

whatchadid.py takes the "-h" or "--help" option to display minimal usage.

If run with no arguments, it looks in the "Documents" folder of your home
directory. If the given a single argument, it reads that as the log file
instead. If the argument is "-", it reads from standard input.

You can optionally change the DELIMITER constant in the code if you need a
different delimiter.

Currently, it does not support filtering and parses the entire log.

Known Deficiencies
------------------

This thing really deserves a decent command line parser. I'll work on that.
