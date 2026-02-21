
#function defination:
#function is a block of code which performs a specific task and can be reused whenever required.

#function call:
#function call is the process of executing a function by its name and passing the required arguments.


def find_highest(list1:list)->int:

    high=list1[0]
    for i in list1:
        if high<i:
            high=i
    return high


list1=[5, 12, 3, 21, 7]
high=find_highest(list1)
print(high)


m=max(list1)
print(m)




def print_stock_prices(stock_prices:dict)->None:
    for i,j in stock_prices.items():
        print(i,j)

def create_portfolio(stock_prices:dict)->list:
    portfolio=[]

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
                portfolio.append(name)
        else:
            print('stock name is invalid type again')
    return portfolio

stock_prices={'tsla':900,'amzn':800,'nifty':1000,'goog':789,'ongc':656}
# print_stock_prices(stock_prices)
# portfolio=create_portfolio(stock_prices)
# print(portfolio)


def add_num(num1:int,num2:int)->int:
    return num1+num2

result=add_num(10,20)
print(result)