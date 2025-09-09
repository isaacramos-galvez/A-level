import datetime
year = input("What year is your next birthday?")
month = input("What month is your next birthday in numbers?")
day = input("What day of the month is your next birthday")

today = datetime.date.today()
birthday = datetime.datetime()
birthday = datetime.datetime(year, month, day)
time_until_birthday = birthday - today
print(time_until_birthday.days)
