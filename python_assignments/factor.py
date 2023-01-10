
user_input = int(input("Enter a number: "))
factor = int(1)
number_of_factors = 0

while factor <= user_input:
    if user_input % factor == 0:
        number_of_factors = number_of_factors + 1
    factor += 1

print(user_input, "has", number_of_factors, "factors")
