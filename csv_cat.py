#!/usr/bin/env python
# CSV module that comes with the Python standard library
import csv
import sys


if __name__ == "__main__":
    # The CSV module exposes a reader object that takes
    # a file object to read. In this example, sys.stdin.
    csvfile = csv.reader(sys.stdin)

    # The script should take one argument that is a column number.
    # Command-line arguments are accessed via sys.argv list.
    column_number = 0
    if len(sys.argv) > 1:
        column_number = int(sys.argv[1])

    # Each row in the CSV file is a list with each
    # comma-separated value for that line.
    for row in csvfile:
        print row[column_number]
