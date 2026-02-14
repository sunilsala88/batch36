
iterable,loopable

a=[22,33,44,55,66]
#type 1 
for p in a:
    print(p)


prices=[5,6,7,8]
total=0
for p in prices:
    total=total+p
print('total is',total)

avg=total/len(prices)
print(avg)


#type 2

print(list(range(5)))
print(list(range(10,15)))
print(list(range(100,150,3)))

for i in range(10):
    print('hello world')


#print all even number from 1 to 100
#get the max value from prices list