# [2015-01-12] Challenge #197 [Easy] ISBN Validator
# http://www.reddit.com/r/dailyprogrammer/comments/2s7ezp/20150112_challenge_197_easy_isbn_validator/

def validate_ISBN(isbn):
    digits = [i for i in isbn if i.isdigit() or i.lower() == 'x']

    if digits[-1].lower() == 'x':
        digits[-1] = '10'

    total = 0
    i = 10
    for digit in digits:
        total += i * int(digit)
        i -= 1

    return (total % 11 == 0)


def main():
    samples_true = ["0495391328", "0716786672", "0471272140"]
    samples_false = ["0495391326", "0716781672", "0471242140"]

    for i in range(len(samples_true)):
        assert validate_ISBN(samples_true[i]) == True
        assert validate_ISBN(samples_false[i]) == False


if __name__ == "__main__":
    main()
