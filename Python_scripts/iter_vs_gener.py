#Iterator way of working

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
mylist = ListIterator(a)
it = iter(mylist)

print("Iterators")
for i in range(len(a)):
    print(next(it))



#Generator of way of working
def list_iterator(list_input):
    for i in list_input:
        yield i
    
a = [1,2,3,4,5,6]
mylist = list_iterator(a)

print("Generators")
for i in mylist:
    print(i)