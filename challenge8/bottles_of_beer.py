# 99 Bottles of beer
# Prints the song "99 Bottles of Beer on the Wall"

for i in range(99,0,-1):
    bottles = i
    left = bottles - 1
    
    line1 = "{} bottles of beer on the wall, {} bottles of beer".format(bottles,bottles)
    line2 = "Take one down, pass it around, {} bottles of beer on the wall".format(left)
    
    if bottles == 1:
        line1 = "{} bottle of beer on the wall, {} bottle of beer".format(bottles,bottles)
        line2 = "Take one down, pass it around, no bottles of beer on the wall".format(left)
    if bottles == 0:
        line1 = "No more bottles of beer on the wall, no more bottles of beer."
        line2 = "Go to the store and buy some more, 99 bottles of beer on the wall."

    print(line1)
    print(line2)
    print("")
