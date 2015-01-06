# [2014-11-10] Challenge #188 [Easy] yyyy-mm-dd
# http://www.reddit.com/r/dailyprogrammer/comments/2lvgz6/20141110_challenge_188_easy_yyyymmdd/

# Not the most elegant solution, but I wanted to play with regex and enums

from enum import Enum
import sys
import re

FILENAME = sys.argv[1]


class Month(Enum):
    Jan, Feb, Mar, Apr, May, Jun = "01", "02", "03", "04", "05", "06"
    Jul, Aug, Sep, Oct, Nov, Dec = "07", "08", "09", "10", "11", "12"


def collect_data(FILENAME):
    """Reads list of dates into a list"""
    data = []
    with open(FILENAME) as in_file:
        for line in in_file:
            data.append(line[:-1])  # remove newline at string's end
    return data


def convert_dates(dates, out_file):
    """Converts given list of dates into format yyyy-mm-dd"""
    for date in dates:
        if re.fullmatch("\d{2}/\d{2}/\d{2}", date):  # format mm/dd/yy
            year = date[-2:]
            month = date[:2]
            day = date[3:5]

            if int(year) >= 50:
                date = "19" + year + '-' + month + '-' + day
            elif int(date[6:]) <= 49:
                date = "20" + year + '-' + month + '-' + day

        elif re.fullmatch("\d{2}#\d{2}#\d{2}", date):  # format mm#yy#dd
            year = date[3:5]
            month = date[:2]
            day = date[-2:]

            if int(year) >= 50:
                date = "19" + year + '-' + month + '-' + day
            elif int(year) <= 49:
                date = "20" + year + '-' + month + '-' + day

        elif re.fullmatch("\d{2}\*\d{2}\*\d{4}", date):  # format dd*mm*yyyy
            year = date[-4:]
            month = date[3:5]
            day = date[:2]
            date = year + '-' + month + '-' + day

        elif re.fullmatch("[A-Z][a-z][a-z]\s\d{2},\s\d{4}", date):  # format word, dd, yyyy
            year = date[-4:]
            month = date[:3]
            day = date[4:6]
            date = year + '-' + Month[month].value + '-' + day

        elif re.fullmatch("[A-Z][a-z][a-z]\s\d{2},\s\d{2}", date):  # format word, dd, yy
            year = date[-2:]
            month = date[:3]
            day = date[4:6]

            if int(year) >= 50:
                date = "19" + year + '-' + Month[month].value + '-' + day
            elif int(year) <= 49:
                date = "20" + year + '-' + Month[month].value + '-' + day

        out_file.write(date + '\n')


date_list = collect_data("dates.txt")
with open("dates_out.txt", 'w') as out_file:
    convert_dates(date_list, out_file)