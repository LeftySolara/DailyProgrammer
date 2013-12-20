# r/dailyprogrammer challenge #3: Caesar Cipher
# User inputs string and the script encrypts it

import string
letters = string.ascii_letters
shift = 6  # number of letters to shift
numbers = (0,1,2,3,4,5,6,7,8,9)

def encode(msg,letters,shift,numbers,new_str):
    for i in msg:
        if i.isalpha() == True:
            index = letters.find(i)
            new_ind = index + shift
            char = letters[new_ind]
            new_str += char
        elif i.isdigit() == True:
            i_int = int(i)
            char = i_int + shift
            if char >= 10:           # keep to one digit
                ch_str = str(char)
                char = ch_str[-1]
            char_str = str(char)
            new_str += char_str
        else:
            new_str += i

    output = new_str.lower()        
    print(output)
    
def decode(msg,letters,shift,numbers,new_str):
    for i in msg:
        if i.isalpha() == True:
            index = letters.find(i)
            new_ind = index - shift
            char = letters[new_ind]
            new_str += char
        elif i.isdigit() == True:
            i_int = int(i)
            num = i_int - shift
            char = str(numbers[num])
            new_str += char
        else:
            new_str += i

    output = new_str.lower()        
    print(output)

def main():
    prompt = input("Enter a string: ")
    option = input("(e)ncode or (d)ecode? ")
    msg = prompt.lower()
    new_str = ""
    
    if option.lower() == "e":
        encode(msg,letters,shift,numbers,new_str)
    elif option.lower() == "d":
        decode(msg,letters,shift,numbers,new_str)
    else:
        print("Invalid option. Try again.")
        
if __name__ == "__main__":
    main()
