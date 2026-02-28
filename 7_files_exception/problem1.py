def print_stock_prices(stock_prices:dict)->None:
    for i,j in stock_prices.items():
        print(i,j)

def create_portfolio(stock_prices:dict)->dict:
    portfolio={}

    while True:

        name=input('enter the name of stock you want to buy (press q to quit)')
        if name.lower()=='q':
            break
        
        if name=='tsla':
            print('cannot trade this stock')
            continue


        found=stock_prices.get(name)
        if found:
            if name in portfolio:
                print('cannot add this stock because it already exist')
            else:
                portfolio.update({name:found})
        else:
            print('stock name is invalid type again')
    return portfolio

def write_to_file(portfolio:dict)->None:
    with open('portfolio.txt','a') as f1:
        for i,j in portfolio.items():
            f1.write(f"{i}: {j} \n")


stock_prices={'tsla':900,'amzn':800,'nifty':1000,'goog':789,'ongc':656}
print_stock_prices(stock_prices)
portfolio=create_portfolio(stock_prices)
print(portfolio)
write_to_file(portfolio)