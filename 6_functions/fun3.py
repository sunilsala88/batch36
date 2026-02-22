

def get_info(name:str,age:int)->None:
    """
    this function takes name and age as input and prints a string with the information
    input: name (string), age (integer)
    output: None
    """
    f=f'{name} is {age} years old'
    print(f)


n='matt'
a=35
get_info(a, n)



def greet(name='friend')->None:
    print("Hello", name)

greet()       # Uses default
greet("Niel") # Uses passed value


#keyword arguments
def display_info(name, city):
    print(f"{name} lives in {city}.")

display_info(city="Mumbai", name="Ravi")
