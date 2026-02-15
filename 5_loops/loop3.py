
stock_prices={'tsla':900,'amzn':800,'nifty':1000}

for k in stock_prices:
    print(k,stock_prices[k])

print(list(stock_prices.keys()))
print(list(stock_prices.values()))
print(list(stock_prices.items()))

#type 4
for i,j in stock_prices.items():
    print(i,j)

num=5

for i in range(1,11):
    print(f'5 * {i}={5*i}')


fact=1
for i in range(1,num+1):
    print(i)
    fact=fact*i
print(fact)