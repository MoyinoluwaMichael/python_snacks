smallest_number = float('+inf')
second_smallest_number = float('+inf')
count = 0

while count < 5:
    user_input = int(input("Enter a number: "))
    if user_input < smallest_number:
        second_smallest_number = smallest_number
        smallest_number = user_input

    if second_smallest_number < user_input < smallest_number:
        second_smallest_number = user_input

    count += 1

print("The smallest number is", smallest_number, "\nWhile the 2nd smallest number is", second_smallest_number, sep=" ")
