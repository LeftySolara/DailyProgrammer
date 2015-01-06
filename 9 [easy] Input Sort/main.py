# [2/17/2012] Challenge #9 [easy]
# http://www.reddit.com/r/dailyprogrammer/comments/pu1rf/2172012_challenge_9_easy/

def prompt():
    temp = input("Enter digits/characters: ")
    items = temp.split()
    return items

def sort(items):
    """ Sorts items in input list and displays contents """
    items.sort()
    for i in items:
        print(i,end=" ")

def main():
    stuff = prompt()
    sort(stuff)

if __name__ == "__main__":
    main()