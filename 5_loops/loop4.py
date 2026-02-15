

a=[22,33,44,55,66]
#type 1
for i in a:
    print(i)


#type 2
for i in range(10):
    print('hello')

#type3 
for i in range(len(a)):
    print(a[i])

#type 4
stock_prices={'tsla':900,'amzn':800,'nifty':1000}
for i,j in stock_prices.items():
    print(i,j)

#first 10 fib number
#0,1,1,2,3,5,8,13,21,34