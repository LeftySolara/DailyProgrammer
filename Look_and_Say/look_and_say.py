def generate_number(n=1, in_str="1", nums=[]):
    """Generates n look-and-say numbers"""

    if len(nums) == n:  # desired number of iterations reached
        return nums

    if in_str == "1" and len(nums) == 0:
        nums.append("1")
        out_str = "1"
        return generate_number(n, out_str, nums)

    digits = list(in_str)
    current = digits[0]
    count = 0
    out_str = ""

    while len(digits) > 0:
        if digits[0] == current:    # digit repeated
            count += 1
            digits.pop(0)
        else:                       # new digit found
            out_str += str(count) + current
            current = digits[0]
            count = 1
            digits.pop(0)

    out_str += str(count) + current
    nums.append(out_str)

    return generate_number(n, out_str, nums)


def main():
    iters = input("Enter number of look-and-say numbers to generate: ")
    if int(iters) < 0:
        print("Invalid argument. Exiting...")
    else:
        numbers = generate_number(int(iters))
        for i in numbers:
            print(i)


if __name__ == '__main__':
    main()