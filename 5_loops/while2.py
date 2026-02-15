stock_prices={'tsla':900,'amzn':800,'nifty':1000,'goog':789,'ongc':656}

for i,j in stock_prices.items():
    print(i,j)

portfolio=[]

while True:

    name=input('enter the name of stock you want to buy (press q to quit)')
    if name.lower()=='q':
        break

    found=stock_prices.get(name)
    if found:
        if name in portfolio:
            print('cannot add this stock because it already exist')
        else:
            portfolio.append(name)
    else:
        print('stock name is invalid type again')

print(portfolio)