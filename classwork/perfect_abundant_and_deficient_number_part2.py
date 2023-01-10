user_input = int(input("Enter a number"))
factor = 1
sum_of_factor = 0
perfect_number = 0
abundant_number = 0
deficient_number = 0

user_response = input("Would you love to submit? ('yes' or 'no'): ")
while user_response == "no":
    while factor < user_input:
        if user_input % factor == 0:
            sum_of_factor += factor
        factor += 1
    if sum_of_factor == user_input:
        perfect_number = user_input
    elif sum_of_factor > user_input:
        abundant_number = user_input
    elif sum_of_factor < user_input:
        deficient_number = user_input
    user_input = int(input("Enter a new number"))
    user_response = input("Would you love to submit? ('yes' or 'no'): ")
    if user_response == "no":
        user_response = "no"
    elif user_response == "yes":
        user_response = "yes"
print(perfect_number, "is a perfect number", sep=" ", end="\n")
print(abundant_number, "is a abundant number", sep=" ", end="\n")
print(deficient_number, "is a deficient number", sep=" ", end="\n")
