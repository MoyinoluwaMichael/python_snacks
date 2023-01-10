count = 0

highest_number = float("-inf")
minimum_number = float("+inf")

while count < 5:
    user_input = int(input("Enter a number: "))
    if user_input > highest_number:
        highest_number = user_input
    if user_input < minimum_number:
        minimum_number = user_input
    count += 1

print("The minimum number is: ", minimum_number)
print("The highest number is: ", highest_number)