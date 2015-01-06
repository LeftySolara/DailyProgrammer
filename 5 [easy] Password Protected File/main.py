# [2/12/2012] Challenge #5 [easy]
# http://www.reddit.com/r/dailyprogrammer/comments/pnhyn/2122012_challenge_5_easy/

from sys import argv
import getpass


def get_login(filename):
    """ Scans text file for usernames and passwords.
        Text file is assumed to be formatted:
        user password """
    users = []
    passwords = []
    with open(filename,'r') as file_obj:
        for i in file_obj:
            split = i.split()
            users.append(split[0])
            passwords.append(split[1])
    return users, passwords


def login(users,passwords):
    """ Login process. User enters name and password,
        boolean returned for login success/failure. """
    uname = input("Enter username: ")
    pwd = getpass.getpass("Enter Password:")
    # check if user and password exist in file
    if uname in users and pwd in passwords:
        # check if user and password match
        if users.index(uname) == passwords.index(pwd):
            return True    # login success
        else:
            return False   # login failed
    else:
        return False


def main():
    script,filename = argv
    users,passwords = get_login(filename)
    log_status = login(users,passwords)
    if log_status == True:
        print("Welcome!")
    elif log_status == False:
        print("Invalid login info. Aborting...")

if __name__ == "__main__":
    main()
