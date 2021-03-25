class Parent:
    def __init__(self, name="Manoj") :
        print("Parent __init__ ", name)
    
class Parent2:
    def __init__(self,name="max"):
        print("Parent2 __init__ ", name)

class Child(Parent,Parent2):
    def __init__(self):
        print("Child __init__")
        super().__init__()
        Parent.__init__(self)
        Parent2.__init__(self,"Ravi")

child = Child()
print(Child.__mro__)