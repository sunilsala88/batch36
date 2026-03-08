
name='sam'
age=30

def sample_function():
    print('This is a sample function')


class Circle:
    pi=3.14

    def __init__(self, radius):
        self.radius = radius  # instance attribute

    def area(self):
        return Circle.pi * (self.radius ** 2)
    
    def circumference(self):
        return 2 * Circle.pi * self.radius