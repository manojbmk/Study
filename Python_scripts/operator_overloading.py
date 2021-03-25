import math

class Circle:
    def __init__(self,radius):
        self.__radius = radius
    
    def setRadius(self,radius):
        self.__radius = radius
    
    def getRadius(self):
       return self.__radius

    def area(self,radius):
        return math.pi* getRadius() ** 2

    def __add__(self,circle_object):
        return Circle(self.__radius + circle_object.__radius) #If you replace + with *, then below c1+c2 will be c1*c2

    def __lt__(self,circle_object):
        return self.__radius < circle_object.__radius ## Change the logic to change the functionality of < 
    
    def __gt__(self,circle_object):
        return self.__radius < circle_object.__radius

c1 = Circle(2)
c2 = Circle(3)
c3 = c1 + c2

print(c3.getRadius())
print(c1 < c2)
print(c3 > c2)