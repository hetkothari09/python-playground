from datetime import datetime
import time

curr_date = datetime(2025, 4, 1, 9, 28, 14)

print(f"The datetime object currently is : {curr_date}")

print(f"After converting it into unix time format the datetime object is: {time.mktime(curr_date.timetuple())}")