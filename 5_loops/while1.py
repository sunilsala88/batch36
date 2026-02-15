
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

l2=[22,33,44,55,66]