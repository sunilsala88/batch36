

import datetime as dt
import time

d1=dt.date(2025,3,28)
print(d1)


t1=dt.time(11,15,10)
print(t1)


dt1=dt.datetime(2026,3,29,11,15,10)
print(dt1)

dd1=dt.timedelta(minutes=5)
print(dd1)



a=dt1.weekday() # 0-6 (0 is Monday, 6 is Sunday)
print(a)


start=dt.datetime(2026,1,1)
thursdays=[]
list1=[start]
for i in range(365):
    start=start + dt.timedelta(days=1)
    list1.append(start)
    if start.weekday()==3:
        thursdays.append(start)

# print(list1)
# print(thursdays)
print(dt.datetime.now())

