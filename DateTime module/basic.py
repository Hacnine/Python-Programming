import datetime
import pytz
dt_dhaka = datetime.datetime.now(tz=pytz.timezone('Asia/Dhaka'))
# print(dt_dhaka.isoformat())

# formatting date and time in specific format
print(dt_dhaka.strftime('%B %d, %Y'))
print(dt_dhaka.strftime('%I:%M:%S %p'))

# convert a date string to date format

date_string = 'December 07, 2020'
dt = datetime.datetime.strptime(date_string, '%B %d, %Y')
print(dt)
