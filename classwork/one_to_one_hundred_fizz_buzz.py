number = 1
while number <= 100:
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number, end="\n")
    number += 1
