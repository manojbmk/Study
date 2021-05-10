#__iter__ and __next__

class ListIterator:

    def __init__(self,list):
        self.__list = list
        self.__index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__index += 1
        if self.__index == len(self.__list):
            raise StopIteration 
        return self.__list[self.__index]
    
a = [1,2,3,4,5,6]
myList = ListIterator(a)
it = myList.__iter__()

print(it.__next__())

print("Remaining keys : ")
for i in it:
    print(i)
