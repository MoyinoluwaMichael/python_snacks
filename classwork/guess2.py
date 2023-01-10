import random

winning_number: int = random.randint(1, 20)

count = 1

print("We warmly welcome you to our guess night.\nWe believe there is no loser here.\n")

user_input = int(input("Enter a number: "))

while count < 5:
    if user_input == winning_number:
        print("Ori e pe bi alajo somolu")
        input("Kindly enter your account details for your cash gift: \n")
        print("Congratulations! Kindly wait as we process your cash gift.")
        break
    elif 20 >= user_input > winning_number or 0 < user_input < winning_number:
        user_input = int(input("Ouch! That's close.\nPlease try again: "))
    else:
        user_input = int(input("Oju e o sha fo bayii.\nTry again: "))

    count += 1
if user_input != winning_number:
    print("We have come to the end of this game, do come back next week for a blast.\nHowever, our winning number is ", winning_number)