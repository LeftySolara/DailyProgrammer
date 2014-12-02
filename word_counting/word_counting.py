"""Given a text file, count how many occurences of each word are present in that text file.

This is by no means an elegant solution, but it does work. I'm hoping to
come back and clean it up a bit at some point (along with most of the code in this repo.
"""

import string

DATA_FILE = "sample_data.txt"
word_list = []
word_count = {}

with open(DATA_FILE, 'r') as in_file:
    for line in in_file:
        for word in line.split():
            word_list.append(word.lower().strip(string.punctuation))

# remove numbers and spaces from count
for word in word_list:
    if word.isdigit() or word == " " or word == "":
        word_list.remove(word)
    else:
        pass

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in word_count:
    print("{} {}".format(word, word_count[word]))