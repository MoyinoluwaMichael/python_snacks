star = "*"
first_star = 10
second_star = 1
print(f"{star:^20}")
count = 1
while count < 10:
    first_star -= 1
    print(star.rjust(first_star), star.rjust(second_star))
    second_star += 2
    count += 1
print(f"{star:.^19}")
