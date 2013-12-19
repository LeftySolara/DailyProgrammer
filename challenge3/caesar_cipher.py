# r/dailyprogrammer challenge #3: Caesar Cipher
# User inputs string and the script encrypts it
# Future plans:
#    - add decript function
#    - add error checking

import string
letters = string.ascii_letters

prompt = input("Enter string to encode: ")
msg = prompt.lower()
let_shift = 6  # number of letters to shift in alpahbat
numbers = (4,5,6,7,8,9,0,1,2,3)
new_str = ""

for i in msg:
    if i.isalpha() == True:
        index = letters.find(i)
        new_ind = index + let_shift
        char = letters[new_ind]
        new_str += char
    elif i.isdigit() == True:
        i_int = int(i)
        index = numbers.index(i_int)
        char = str(index)
        new_str += char
    else:
        new_str += i

output = new_str.lower()        
print(output)
