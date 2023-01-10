
user_input = 1
even_number = 0
odd_number = 0
sum_even_number = 0
sum_odd_number = 0
while user_input > 0:
    user_input = int(input("Enter a number, enter any negative number to exit\n"))
    if user_input < 0:
        break
    elif user_input % 2 == 0:
        even_number += 1
        sum_even_number += user_input
    elif user_input % 2 > 0:
        odd_number += 1
        sum_odd_number += user_input

print("Number of odd numbers entered is", odd_number, "\nNumber of even numbers is", even_number,
      "\nSum of odd numbers is", sum_odd_number, "\nSum of even numbers is", sum_even_number, sep=" ")