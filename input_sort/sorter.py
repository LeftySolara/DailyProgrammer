# r/dailyprogrammer challenge #9 (easy)
# takes user input and sorts numerically/alphabetically

def prompt():
	temp = input("Enter digits/characters: ")
	items = temp.split()
	return items

def sort(items):
	""" Sorts items in input list and displays contents """
	items.sort()
	for i in items:
		print(i,end=" ")

def main():
	stuff = prompt()
	sort(stuff)

if __name__ == "__main__":
	main()