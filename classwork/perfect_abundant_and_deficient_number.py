user_input = int(input("Enter a number: "))
factor = 1
sum_of_factor = 0
while factor < user_input:
    if user_input % factor == 0:
        sum_of_factor += factor
    factor += 1

if sum_of_factor == user_input:
    print(user_input, "is a perfect number")
elif sum_of_factor > user_input:
    print(user_input, "is an abundant number")
elif sum_of_factor == user_input:
    print(user_input, "is a deficient number")