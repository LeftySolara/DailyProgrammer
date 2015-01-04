# [2015-01-02] Challenge #195 [All] 2015 Prep Work
# http://www.reddit.com/r/dailyprogrammer/comments/2r4wal/20150102_challenge_195_all_2015_prep_work/

# This code is not meant to be imported. It is only here for reference and copy/paste jobs.

# Methods to write:
#   - find permutations
#   - strip punctuation from string
#   - determine if a number is prime
#   - determine if input is a pallendrome
#   - swap data in variables

IN_FILE  = "Latin-Lipsum.txt"
OUT_FILE = "output.txt"
DATA = ["This is the first line.\n", "This is the second line.\n", "This is the third line.\n"]

import random

class InputOutput():
    """Code for  dealing with user and file i/o."""

    def read_file(self, filename):
        """Open a text file and save contents as list of lines"""
        with open(filename,'r') as myFile:
            lines = myFile.readlines()
        return lines

    def write_file(self, data, filename):
        """Write data to output file. Assumes data is iterable."""
        with open(filename,'w') as out_file:
            for i in data:
                out_file.write(str(i))

    def read_user_input(self):
        """read user input from the console."""
        in_data = input("Enter some data: ")
        return in_data


class StringManip():
    """Code for dealing with and manipulation strings."""

    def reverse_string(self, string):
        string = string[::-1]
        return string

    def convert_case(self, string):
        string = string.lower()
        string = string.upper()
        return string


class NumberMethods():
    """Code for dealing with numbers of any kind."""

    def generate_random_number(self):
        return random.randrange(1,100)

    def reverse_number(self, number):
        number = int(str(number)[::-1])
        return number

class Algorithms():
    """General algorithms"""

    def is_palendrome(self, data):
        return str(data)[::-1] == str(data)

    def choose_random_value(self, data):
        """Choose a random value from a container"""
        return random.choice(data)

def main():
    ioTests = InputOutput()
    stringTests = StringManip()
    numTests = NumberMethods()
    algorithmTests = Algorithms()

    assert len(ioTests.read_file(IN_FILE)) == 48
    ioTests.write_file(DATA, OUT_FILE)

    assert stringTests.reverse_string("Hello") == "olleH"
    assert stringTests.convert_case("Hello") == "HELLO"

    assert 1 <= numTests.generate_random_number() <= 100
    assert numTests.reverse_number(123456789) == 987654321

    assert algorithmTests.is_palendrome("World") == False
    assert algorithmTests.is_palendrome("12321") == True
    assert algorithmTests.choose_random_value(DATA) in DATA

if __name__ == '__main__':
    main()