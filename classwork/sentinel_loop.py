positive_number = int(input("Enter a positive number: "))

while positive_number <= 0:
	positive_number = int(input("Fool! That's a negative number, please try again: \n"))

else:
	print("Great! You have entered a positive number")