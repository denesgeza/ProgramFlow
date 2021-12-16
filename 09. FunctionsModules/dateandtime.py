import time
import datetime as dt

# print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))

# print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

# if time.daylight != 0:
#     print("DST in effect!")
#     print(f"DST time zone is {time.tzname[1]}")

print(dt.datetime.today())
print(dt.datetime.now())
