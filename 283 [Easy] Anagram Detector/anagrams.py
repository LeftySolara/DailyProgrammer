def is_anagram(string1, string2):
    words1 = string1.lower().split(' ')
    words2 = string2.lower().split(' ')
    any_in = bool(set(words1).intersection(set(words2)))

    string1 = sorted([ch for ch in string1.lower() if ch.isalpha()])
    string2 = sorted([ch for ch in string2.lower() if ch.isalpha()])
    return (not any_in) and (string1 == string2)


def main():
    input_file = open("challenge_input.txt")
    for line in input_file:
        words = line.strip().replace('"', '').split(' ? ')
        anargam = is_anagram(words[0], words[1])
    
        if anargam:
            indicator = "is"
        else:
            indicator = "is NOT"
    
        print('"{}" {} an anagram of "{}"'.format(words[0], indicator, words[1]))
    input_file.close()


if __name__ == '__main__':
    main()