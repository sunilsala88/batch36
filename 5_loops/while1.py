
number=1

while True:
    if number==5:
        break
    print(number)
    number=number+1

print('last line')


fib=[0,1]
num1=fib[0]
num2=fib[1]

for i in range(8):
    current=num1+num2
    fib.append(current)
    num1=num2
    num2=current
print(fib)


fib=[0,1]
num1=fib[0]
num2=fib[1]
count=0
while True:
    if count==8:
        break
    count=count+1
    current=num1+num2
    fib.append(current)
    num1=num2
    num2=current
print(fib)

l2=[22,33,44,55,66,77,88]
l=list(range(len(l2)-1,-1,-1))
print(l)
rev_list=[]
for i in l:
    rev_list.append(l2[i])
print(rev_list)

new=[]
index1=len(l2)
while True:
    index1=index1-1
    new.append(l2[index1])
    if index1==0:
        break
print(new)

#5 element
#4,3,2,1,0
#-1,-2,-3,-4,-5