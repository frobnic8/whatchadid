whatchadid
==========

Parse a WhatchDoingLog.XML into a comma delimited text file.

The default export as CSV or XLS from WhatchaDoing is broken. This processes
the log file using BeautifulSoup 4 to produce a CSV.

Installation
------------
If you don't have BeautifulSoup 4, run:

    pip install bs4

Or, if you aren't using virtualenv for example, try:

    sudo pip install bs4

If you don't have pip, pester Erskin or go here:

    http://www.pip-installer.org/en/latest/installing.html

Alternatively, feel free to rewrite this to not need BeautifulSoup if you have
too much time on your hands. ;)

Usage
-----
whatchadid.py takes the "-h" or "--help" option to display minimal usage.
If run with no arguments, it looks in the "Documents" folder of your home
directory. If the given a single argument, it reads that as the log file
instead. If the argument is "-", it reads from standard input.

You can optionall change the DELIMITER constant in the code if you need a
different delimiter.
