
import datetime as dt

epoch1=1774690562
dt1=dt.datetime.fromtimestamp(epoch1)
print(dt1)

epoch2=dt1.timestamp()
print(epoch2)


#str
s1="2025/03/28 11:15:10"
f='%Y/%m/%d %H:%M:%S'
dt2=dt.datetime.strptime(s1,f)  
print(dt2)

#datetime to string
dt4=dt1.strftime('%Y==%m')
print(dt4)