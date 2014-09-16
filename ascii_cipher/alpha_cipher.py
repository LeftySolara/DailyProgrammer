# r/dailyprogrammer challenge #3 (intermediate)
# ascii substitution cipher

import re

def prompt():
	""" Prompt user for input """

	usr_in = input("Enter a sequence of characters: ")
	in_list = re.split("(\s)",usr_in)
	return in_list

def encode(usr_list):
	""" Swaps characters in user input """

	new_list = []
	for item in usr_list:
		temp = ""
		for k in item:
			index = item.index(k)
			place = ord(k) + 7
			k = chr(place)
			temp += k
		new_list.append(temp)
	return new_list

def decode(usr_list):
	""" Swaps characters in user input """

	new_list = []
	for item in usr_list:
		temp = ""
		for k in item:
			index = item.index(k)
			place = ord(k) - 7
			k = chr(place)
			temp += k
		new_list.append(temp)
	return new_list

def main():
	stream = prompt()
	option = input("Encode or decode? ")
	if option.lower() == "encode":
		new = encode(stream)
		for i in new:
			print(i,end="")
	elif option.lower() == "decode":
		old = decode(stream)
		for t in old:
			print(t,end="")
	print("")

if __name__ == "__main__":
	main()