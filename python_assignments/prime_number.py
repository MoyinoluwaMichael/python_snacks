
user_input = int(input("Enter a number: "))
number_of_factor = 0
factor = 1

while factor <= user_input:
    if user_input % factor == 0:
        number_of_factor += 1
    factor += 1

if number_of_factor == 2:
    print(user_input, "is a prime number", sep=" ")
else:
    print(user_input, "is not a prime number", sep=" ")
