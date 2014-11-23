"""Read in dates, output in format yyyy-mm-dd"""

from enum import Enum
import sys

FILENAME = sys.argv[1]

class Months(Enum):
    JAN, FEB, MAR, APR, MAY, JUN = 1, 2, 3, 4, 5, 6
    JUL, AUG, SEP, OCT, NOV, DEC = 7, 8, 9, 10, 11, 12


def collect_data(FILENAME):
    """Reads list of dates into a list"""
    data = []
    with open(FILENAME) as in_file:
        for line in in_file:
            data.append(line[:-1])  # remove newline at string end
    return data

    
# data = collect_data("dates.txt")
# for i in data:
#     print(i)