number_of_positives = 0
number_of_negatives = 0
total = 0
user_input = int(input("Enter an integer, the input ends if it is 0: "))
if user_input == 0:
    print("No numbers are entered except 0")

while user_input != 0:
    if user_input > 0:
        number_of_positives += 1
    else:
        number_of_negatives += 1
    total += user_input
    user_input = int(input("Enter an integer, the input ends if it is 0: "))

average = total/(number_of_positives+number_of_negatives)

print(f"The number of positives is {number_of_positives}\nThe number of negatives is {number_of_negatives}\nThe total "
      f"is {total}\nThe average is {round(average, 2)}")
