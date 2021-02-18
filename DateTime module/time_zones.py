import datetime
import pytz

# for time zone
dt = datetime.datetime(2020, 7, 12, 9, 30, 45, tzinfo=pytz.UTC)
# print(dt)

# to  print list of the time zone name
for timezone in pytz.all_timezones:
    # print(timezone)
    pass

# dt_utc_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utc_now)
#
# dt_dhaka = dt_utc_now.astimezone(pytz.timezone('Asia/Dhaka'))
# print(dt_dhaka)

dt_utc_now = datetime.datetime.now()
# print(dt_utc_now)
dt_dhaka = dt_utc_now.astimezone(pytz.timezone('US/Eastern'))
print(dt_dhaka)
