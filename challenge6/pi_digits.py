# r/dailyprogrammer challenge #6: pi calculator
# calculates pi to the nth digit using the Baily-Borwein-Plouffe formula

from decimal import getcontext

def calculate(n,digits):
    """ Calculates step n in the Baily-Borwein-Plouffe summation. """
    getcontext().prec = digits
    x = 8*n
    a = 1/(16**n)
    b = 4/(x+1)
    c = 2/(x+4)
    d = 1/(x+5)
    e = 1/(x+6)
    ans = a*(b-c-d-e)
    
    return ans


def main():
    prompt = input("Calculate to how many decimal places? ")
    digits = int(prompt)
    pi = 0
    for n in range (0,digits+1):
        step = calculate(n,digits)
        pi += step
    
    print("Pi to {} decimal places is: {:.{}f}".format(digits,pi,digits))

if __name__ == "__main__":
    main()
