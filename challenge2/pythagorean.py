""" Pythagorean calculator. Creates an object of class Triangle and solves
    for the third side. """

import math

class Triangle():

    def __init__(self,a=0,b=0,c=0):
        sides = [float(a),float(b),float(c)]
        self.__unknowns = [i for i in sides if i == 0]
        self.__knowns = [x for x in sides if x != 0]
        self.__variable = self.__unknowns[0]

    def __str__(self):
        sides_str = ("Side A = {}\nSide B = {}\nSide C = {}"
                     .format(self.__knowns[0],self.__knowns[1],self.__knowns[2]))
        return sides_str

    def pythagorean(self):
        if len(self.__unknowns) == 1:
            self.__variable = math.sqrt(self.__knowns[0]**2 + self.__knowns[1]**2)
            self.__knowns.append(self.__variable)
        solved_str = "Unknown side = {}".format(self.__variable)
        return solved_str


def main():
    print("Pythagorean calculator. Enter side lengths at prompts (enter 0 for unknowns).")
    a = input("Enter length of side 1: ")
    b = input("Enter length of side 2: ")
    c = input("Enter length of side 3: ")

    triangle = Triangle(a,b,c)
    triangle.pythagorean()
    print(triangle)

main()
