user_input = int(input("Enter number: "))
count = int(1)
while count <= 12:
    result = user_input * count
    print(user_input, "times", count, "is", result, sep=" ", end='\n')
    count += 1