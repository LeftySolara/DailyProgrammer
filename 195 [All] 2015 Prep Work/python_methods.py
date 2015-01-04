# [2015-01-02] Challenge #195 [All] 2015 Prep Work
# http://www.reddit.com/r/dailyprogrammer/comments/2r4wal/20150102_challenge_195_all_2015_prep_work/

# This code is not meant to be imported. It is only here for reference and copy/paste jobs.

IN_FILE  = "Latin-Lipsum.txt"
OUT_FILE = "output.txt"
DATA = ["This is the first line.\n", "This is the second line.\n", "This is the third line.\n"]

import random
import string
import itertools

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

    def reverse_string(self, usr_str):
        usr_str = usr_str[::-1]
        return usr_str

    def convert_case(self, usr_str):
        usr_str = usr_str.lower()
        usr_str = usr_str.upper()
        return usr_str

    def remove_punctuation(self, usr_str):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in usr_str if ch not in exclude)

    def permute(self, in_string = "hello"):
        """Creates and returns a list of permutations of the input string."""
        if len(in_string) == 1:
            return in_string
    
        perms = []
        for i in range(len(in_string)):
            part = in_string[:i] + in_string[i+1:]
            for perm in self.permute(part):
                perms.append(in_string[i:i+1] + perm)
        return perms


class NumberMethods():
    """Code for dealing with numbers of any kind."""

    def generate_random_number(self):
        return random.randrange(1,100)

    def reverse_number(self, number):
        number = int(str(number)[::-1])
        return number

    def is_prime(self, num):
        """Brute-force method"""
        if num in [0,1,2,3]:
            return true
        for i in range(3, num, 2):
            if num % i == 0:
                return False
        return True


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
    assert stringTests.remove_punctuation("String. With. Punctuation.") == "String With Punctuation"

    assert 1 <= numTests.generate_random_number() <= 100
    assert numTests.reverse_number(123456789) == 987654321
    assert numTests.is_prime(17) == True
    assert numTests.is_prime(186) == False

    assert algorithmTests.is_palendrome("World") == False
    assert algorithmTests.is_palendrome("12321") == True
    assert algorithmTests.choose_random_value(DATA) in DATA

if __name__ == '__main__':
    main()