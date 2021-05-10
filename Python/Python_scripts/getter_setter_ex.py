class Car:
    def __init__(self,speed,colour):
        self.__speed = speed
        self.__colour = colour

    def set_speed(self,value):
        self.__speed = value
    
    def get_speed(self):
        return self.__speed

audi = Car(200,'red')
benz = Car(250,'black')

print(audi.get_speed())

audi.__speed = 300

print(audi.get_speed())

audi.set_speed(300)
print(audi.get_speed())