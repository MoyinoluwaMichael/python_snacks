import random

number_of_guesses = 1

winning_number = random.randint(1,100)


while number_of_guesses < 3:
    guess = int(input("Enter a number between 1 and 100: "))
    if guess == winning_number:
        print("Awesome!\nYou are right")
        break
    else:
        guess = int(input("Guess a number between 1 and 100: "))
    number_of_guesses += 1

print("Eeyah, that's wrong!\ntake heart dear.\nThe winning number is ", winning_number)

