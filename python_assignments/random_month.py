import random

random_number = random.randint(1, 12)
month = ""
if random_number == 1:
    month = "January"
elif random_number == 2:
   month = "February"
elif random_number == 3:
    month = "March"
elif random_number == 4:
    month = "April"
elif random_number == 5:
    month = "May"
elif random_number == 6:
    month = "June"
elif random_number == 7:
    month = "July"
elif random_number == 8:
    month = "August"
elif random_number == 9:
    month = "September"
elif random_number == 10:
    month = "October"
elif random_number == 11:
    month = "November"
elif random_number == 12:
    month = "December"

print(month)