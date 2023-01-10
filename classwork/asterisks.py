def print_right_angle_asterisks(number: int):
    for row in range(1, number + 1):
        print("* " * row, end="\n")


def print_square_asterisks(number: int):
    for row in range(1, number + 1):
        if row == 1 or row == number:
            print("*   " * number)
        else:
            print("*", " " * ((number - 2) * 4), "   *", sep="")


def print_diamond_asterisks(number: int):
    space1 = number * 3
    space2 = 0
    for row in range(number):
        if row == 0:
            print(" " * space1, "*", end="")
        else:
            print(" " * space1, end="")
            for column in range(2):
                print("*", end=" ")
                print(" " * space2, end="")
        space1 -= 2
        space2 += 4
        print()
    print(" "*space1, "*", " "*(space2+1), "*", sep="")
    for row in range(number):
        space1 += 2
        space2 -= 4
        if row == number -1:
            print(" "*(space1+1), "*", sep="")
        else:
            print(" "*space1, end="")
            print("*", end="")
            print(" "*space2, "*", end="")
            print()


# print_right_angle_asterisks(10)
print()
# print_square_asterisks(5)
# print()
print_diamond_asterisks(10)
