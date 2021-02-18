
from datetime import time, date
import datetime

tme = time(9, 30, 45, 100000)
# print(tme)
# print(tme.hour)
# print(tme.minute)

date_time = datetime.datetime(2020, 7, 12, 9, 30, 45, 100000)
# print(date_time.date())
print(date_time)
# print(date_time.time())
# print(date_time.year)

t_delta = datetime.timedelta(days=7)
# t_delta = datetime.timedelta(hours= 12)

# date after 1 week
future_date = date_time + t_delta
# print(future_date)

d_time = datetime.date(2002, 7, 12)
t_day = datetime.date.today()

# print(t_day.weekday())
# print(t_day.isoweekday())
# print(t_day.isoweekday())

t_delta = datetime.timedelta(days=7)
# date after 1 week
future_date = t_day + t_delta

# date before 1 week
past_date = t_day - t_delta
# print(past_date)

last_day = datetime.date(2020, 12, 31)
reaming_day = last_day - t_day
# print(reaming_day)
# print(reaming_day.total_seconds())



# importing date class

## Since we know the number, we can save them in a list and print the day on that number
day = ["0", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

## Creating an instance
x = date.today()
d = x.isoweekday()
# print("Today's isoweekday number is:", d)
# print("Today's day is:", day[d])

x = date(2020, 1, 1)
# print("Day on", x.year, "new year was:", day[x.isoweekday()])

x = date(2021, 1, 1)
# print("Day on", x.year, "new year will be:", day[x.isoweekday()])
