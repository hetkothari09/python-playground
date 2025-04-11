from datetime import datetime, tzinfo
import pytz
import time

unaware_timezone = datetime.now()
print(f"The naive timezone is : {unaware_timezone}" )

aware_timezone_utc = datetime.now(pytz.utc)
print(f"The utc aware timezone is : {aware_timezone_utc}")

aware_timezone_america = datetime.now(pytz.timezone('US/CENTRAL'))
print(f"The US/CENTRAL aware time zone is : {aware_timezone_america}")

print(aware_timezone_america.tzname())
print(aware_timezone_utc.tzname())

print(aware_timezone_utc.dst())
print(aware_timezone_america.dst())

print(aware_timezone_utc.utcoffset())
print(aware_timezone_america.utcoffset())

print("\n\nConverting time zones:")

timezone_india = datetime.now(pytz.timezone('ASIA/KOLKATA'))
timezone_usa_central = timezone_india.astimezone(pytz.timezone('US/CENTRAL'))
timezone_usa_newyork = timezone_usa_central.astimezone(pytz.timezone('AMERICA/NEW_YORK'))
timezone_usa_mexico = timezone_usa_newyork.astimezone(pytz.timezone('AMERICA/MEXICO_CITY'))


print(timezone_india.strftime('%d-%B-%Y %H:%M:%S'))
print(timezone_usa_central.strftime('%d-%B-%Y %H:%M:%S'))
print(timezone_usa_newyork.strftime('%d-%B-%Y %H:%M:%S'))
print(timezone_usa_mexico.strftime('%d-%B-%Y %H:%M:%S'))