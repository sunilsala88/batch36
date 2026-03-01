#what is class
#class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. 
# A class can be thought of as a template for creating objects, and an object is an instance of a class.

#what is object
#An object is an instance of a class. It is a specific realization of a class,

#attribute
#any variable that is defined inside a class is called an attribute. Attributes can be used to store data about the object.

#class attribute
#A class attribute is an attribute that is shared by all instances of a class.

#instance attribute
#An instance attribute is an attribute that is specific to a particular instance of a class. Each

#method
#A method is a function that is defined inside a class. 
# Methods are used to perform operations on the attributes of the class and to define the behavior of the objects created from the class.

#__init__ method(constructor)
#The __init__ method is a special method in Python classes. 
# It is called when an object is created from the class and is used to initialize the attributes of the object.
class Student:
    school_name="ABC School" #class attribute
    
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {Student.school_name}")

s1=Student("Alice", 14)
s2=Student("Bob", 15)

print(s1.name) # Output: Alice
print(s2.name) # Output: Bob
print(s1.school_name)
print(s2.school_name)

s1.display_info() # Output: Name: Alice, Age: 14, School: ABC School


class Circle:
    pi=3.14

    def __init__(self, radius):
        self.radius = radius  # instance attribute

    def area(self):
        return Circle.pi * (self.radius ** 2)
    
    def circumference(self):
        return 2 * Circle.pi * self.radius
    

c1=Circle(5)
print(c1.area()) # Output: 78.5
print(c1.circumference()) # Output: 31.400000000000002


