# r/dailyprogrammer challenge #4 - Random password generator
# Creates specified number of passwords of specified length
# Appends passwords to file "passwords.txt"

import string
import random

characters = string.ascii_letters + "0123456789!@#$%&"
pass_len = input("How many characters per password? ")
pass_num = input("How many passwords? ")
sites = input("Name sites (y/n)? ")

def gen(pass_len,pass_num,characters):
    password = ""
    for i in range(int(pass_len)):
        char = random.choice(characters)
        password += char
    return password

def write_file(site,passwd):
    with open("passwords.txt","a") as file_obj:
        file_obj.write("{:>10}  {:<12}\n".format(site,passwd))
        
def main(pass_len,pass_num,characters):
    if sites.lower() == "y":
        for c in range(int(pass_num)):
            site = input("Site name: ")
            passwd = gen(pass_len,pass_num,characters)
            write_file(site,passwd)
    elif sites.lower() == "n":
        for c in range(int(pass_num)):
            site = ""
            passwd = gen(pass_len,pass_num,characters)
            write_file(site,passwd)
    else:
        print("Invalid option. Try again.")

if __name__ == "__main__":
    main(pass_len,pass_num,characters)
