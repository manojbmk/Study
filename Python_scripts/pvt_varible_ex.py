class Hello:
    def __init__(self,name):
        self.a = 10
        self._b = 20
        self.__c = 30
    
    def one(self):
        self.__private_method()
        print(self.__c)

    def __private_method(self):
        print("This is a private method")
    
hello = Hello('manoj')
print(hello.a)
print(hello._b)
hello.one()
