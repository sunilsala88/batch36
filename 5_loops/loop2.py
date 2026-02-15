


prices=[33,77,99,22,55]
max=prices[0]
for p in prices:
    if p>max:
        max=p
print(max)

#type3
stock_name=['ongc','reliance','goog','amzn']

for i in range(4):
    print(stock_name[i])

print('-----')
#type 1
for i in stock_name:
    print(i)


prices=[11,33,55]
volumes=[100,200,300]

num=0
den=0
for i in range(3):
    p=prices[i]
    v=volumes[i]
    num=num+p*v
    den=den+v

vwap=num/den
print(vwap)
