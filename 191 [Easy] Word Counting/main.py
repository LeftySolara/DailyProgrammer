# [2014-12-1] Challenge #191 [Easy] Word Counting
# http://www.reddit.com/r/dailyprogrammer/comments/2nynip/2014121_challenge_191_easy_word_counting/

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