from datetime import datetime
def find_birthday():

    year = int(input("What year is your next birthday?"))
    month = int(input("What month is your next birthday in numbers?"))
    day = int(input("What day of the month is your next birthday"))

    birthday = datetime(2000 + year, month, day)
    return birthday

def calculate_days(birthday, today):
    this_year = datetime(today.year, birthday.month, birthday.day)
    next_year = datetime(today.year + 1, birthday.month, birthday.day)

    return ((this_year if this_year > today else next_year) - today).days
   
today = datetime.today()
a = find_birthday()
b = calculate_days(a, today)

print(b)