
import datetime as dt

d1=dt.datetime.now(tz=dt.timezone.utc)
print(d1)
print('current_time',dt.datetime.now())

from zoneinfo import ZoneInfo
new_york_timezone = ZoneInfo('America/New_York')
kolkata_timezone = ZoneInfo('Asia/Kolkata')

print(dt.datetime.now(tz=new_york_timezone))
print(dt.datetime.now(tz=kolkata_timezone))
print('--------------------'*5)
#pendulum
import pendulum
dt1=pendulum.now('Asia/Kolkata')
print(dt1)
dt2=pendulum.now('America/New_York')
print(dt2)
dt3=pendulum.now('UTC')
print(dt3)