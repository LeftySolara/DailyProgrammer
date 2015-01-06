# Challenge #8 [easy]
# http://www.reddit.com/r/dailyprogrammer/comments/pserp/2162012_challenge_8_easy/

def main():
    for i in range(99,0,-1):
        bottles = i
        remaining = bottles - 1
        
        line1 = "{} bottles of beer on the wall, {} bottles of beer".format(bottles,bottles)
        line2 = "Take one down, pass it around, {} bottles of beer on the wall".format(remaining)

        if bottles == 2:
            line1 = "{} bottles of beer on the wall, {} bottles of beer".format(bottles,bottles)
            line2 = "Take one down, pass it around, {} bottle of beer on the wall".format(remaining)
        
        if bottles == 1:
            line1 = "{} bottle of beer on the wall, {} bottle of beer".format(bottles,bottles)
            line2 = "Take one down, pass it around, no bottles of beer on the wall".format(remaining)
        if bottles == 0:
            line1 = "No more bottles of beer on the wall, no more bottles of beer."
            line2 = "Go to the store and buy some more, 99 bottles of beer on the wall."
    
        print(line1)
        print(line2)
        print("")


if __name__ == "__main__":
    main()
