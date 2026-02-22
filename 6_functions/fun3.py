

# def get_info(name:str,age:int)->None:
#     """
#     this function takes name and age as input and prints a string with the information
#     input: name (string), age (integer)
#     output: None
#     """
#     f=f'{name} is {age} years old'
#     print(f)


# n='matt'
# a=35
# get_info(a, n)



# def greet(name='friend')->None:
#     print("Hello", name)

# greet()       # Uses default
# greet("Niel") # Uses passed value


# #keyword arguments
# def display_info(name, city):
#     print(f"{name} lives in {city}.")

# display_info(city="Mumbai", name="Ravi")




def intro(stock_name,stock_price):
    print(f" stock name is {stock_name} and stock price is {stock_price}")
    # print(" stock name is" ,stock_name," and stock price is ",stock_price)

#positional argument
intro('tsla',500)
intro(500,'tsla')

#keyword argument
intro(stock_price=500,stock_name='tsla')



#default argument

def intro(stock_name='sp500',stock_price=5000):
    print(f" stock name is {stock_name} and stock price is {stock_price}")
    # print(" stock name is" ,stock_name," and stock price is ",stock_price)

intro()
intro('amzn')
intro('amzn',1000)