def calculate_future_day(current_date: int, number: int):
    future_day = ""
    future_date = (current_date + number) % 7
    if future_date == 0:
        future_day = "Sunday"
    elif future_date == 1:
        future_day = "Monday"
    elif future_date == 2:
        future_day = "Tuesday"
    elif future_date == 3:
        future_day = "Wednesday"
    elif future_date == 4:
        future_day = "Thursday"
    elif future_date == 5:
        future_day = "Friday"
    elif future_date == 6:
        future_day = "Saturday"
    return future_day


current_date = int(input("Enter today's day: "))
while current_date > 6 or current_date < 0:
    current_date = int(input("Ode ni e\nEnter a number between 0 and 6 for today's day of the week: "))
# if current_date == 0:
#     current_day = "Sunday"
# elif current_date == 1:
#     current_day = "Monday"
# elif current_date == 2:
#     current_day = "Tuesday"
# elif current_date == 3:
#     current_day = "Wednesday"
# elif current_date == 4:
#     current_day = "Thursday"
# elif current_date == 5:
#     current_day = "Friday"
# elif current_date == 6:
#     current_day = "Saturday"

future_date_count = int(input("Enter the number of days elapsed since today: "))
# future_date = current_date
# for count in range(0, future_date_count, 1):
#     future_date += 1
#     if future_date == 7:
#         future_date = 0
current_day = calculate_future_day(current_date, 0)
future_day = calculate_future_day(current_date, future_date_count)

print(f"Today is {current_day} and the future day is {future_day}")

match current_date:
    case 2:
        print("Great")
