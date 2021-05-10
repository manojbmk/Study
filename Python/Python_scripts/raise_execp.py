class CoffeeCupHotException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class CoffeeCupHotException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class CoffeeCup:
    def __init__(self,temperature):
        self.__temperature = temperature
    
    def drink_coffee(self):
        if self.__temperature > 85:
            print("Coffee Too Hot")
            raise CoffeeCupHotException('Coffee Too hot')

        elif self.__temperature < 65:
            print("Coffee is cold")
            raise ZeroDivisionError
        else:
            print("Coffee is okay to drink")
        finally:
            print("Always executes")
            print(cup.__temperature)
try:
    cup = CoffeeCup(788)
    cup.drink_coffee()
except ZeroDivisionError:
    print("exception riased from above class")