for number in range(1, 101, 1):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number, end="\n")
    number += 1
