
largest_number = float('-inf')
smallest_number = float('+inf')
iteration = True

while iteration:
    user_input = int(input("Enter a number: "))
    if user_input > largest_number:
        largest_number = user_input
    if user_input < smallest_number:
        smallest_number = user_input
    if_done = input("Would you love to submit? (yes or no): ")
    if if_done == "yes":
        iteration = False
    elif if_done == "no":
        iteration = True
    while if_done != "yes" and if_done != "no":
        user_input2 = input("Error!\nWould you love to submit? (yes or no): ")
        if user_input2 == "yes":
            if_done = "yes"
            iteration = False
        elif user_input2 == "no":
            if_done = "no"
            iteration = True

print("The largest number is", largest_number, sep=" ")
print("The smallest number is", smallest_number, sep=" ")
