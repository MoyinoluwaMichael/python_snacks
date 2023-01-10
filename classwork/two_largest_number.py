count = 0

largest_number = float('-inf')
second_largest_number = float('-inf')
smallest_number = float('+inf')

while count < 5:
    user_input = int(input("Enter a number: "))
    if user_input > largest_number:
        second_largest_number = largest_number
        largest_number = user_input
    if user_input < largest_number and user_input > second_largest_number:
        second_largest_number = user_input
    if user_input < smallest_number:
        smallest_number = user_input

    count += 1
if largest_number != smallest_number and smallest_number != second_largest_number:
    print("The largest number is", largest_number, "\nThe second largest number is", second_largest_number, sep=" ")
    print("While the smallest number is", smallest_number, sep=" ")

elif second_largest_number == smallest_number:
    print("The largest number is", largest_number, sep=" ")
    print("Guy, there is no second largest and smallest number")


else:
    print("Guy, the numbers are same")
