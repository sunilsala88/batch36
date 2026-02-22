

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
intro('tsla',1000)




def sum_numbers(*yy):
    print(yy)
    return sum(yy)

a=sum_numbers(1,2,4,5)
print(a)

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Anil", age=30, country="India")

def outer():
    def inner():
        print("Inner function executed.")
    inner()
    print("Outer function executed.")

outer()

def get_fib(number:int)->list:

    fib=[0,1]
    num1=fib[0]
    num2=fib[1]


    for i in range(number-2):
        num3=num1+num2
        fib.append(num3)
        num1=num2
        num2=num3
    return fib


l=get_fib(10)

print(l)

#rev_string
def rev_string(word:str)->str:

    l=len(word)
    final=""
    for i in range(-1,-(l+1),-1):
        final=final+word[i]
    return final

r=rev_string('hello')
print(r)