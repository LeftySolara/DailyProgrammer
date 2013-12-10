"""
r/dailyprogrammer challenge #1: Reddit user info

Goal:
Create a program that will ask for a user's name, age, and reddit username. Log info in a file.
Have it tell them the information back in the format:
    Your name is (name)
    You are (age) years old
    Your username is (username)
"""

def get_info():
    name_str = input("What is your name? ")
    name = name_str.capitalize()
    age = input("How old are you? ")
    username = input("What is your reddit username? ")
    with open("reddit_info.txt", "a") as file_obj:
        file_obj.write("\n{:<12} {:^6} {:<10} ".format(name,age,username))
    show(name,age,username)

def show(name,age,username):
    print()
    print("Your name is {}".format(name))
    print("You are {} years old".format(age))
    print("Your username is {}".format(username))

get_info()
