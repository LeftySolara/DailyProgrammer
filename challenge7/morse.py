# r/dailyprogrammer challenge #7: morse code translator

code = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----"}

def get_morse(prompt):
    """ Pulls message from file. """
    with open(prompt,"r") as filename:
        line = filename.readline().strip("\n")
    return line
    
def make_string(morse,code):
    """ Converts morse to alphanumeric characters. """
    split = morse.split(" ")
    new_str = ""
    for i in split:
        lkey = [k for k, v in code.items() if v == i]   # find key of morse in dict
        if lkey == []:
            lkey = " "
        new_str += lkey[0]
    return new_str
    
def main():
    prompt = input("Enter filename containing message: ")
    morse = get_morse(prompt)
    message = make_string(morse,code)
    print(message)
    
if __name__ == "__main__":
    main()
