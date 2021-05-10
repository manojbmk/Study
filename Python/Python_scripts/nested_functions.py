#Example 1
def outerFunction(text):  #Enclosing function 
    def innerFunction():  #Local function 
        print(text)
    innerFunction()

outerFunction("Hello")


##Example 2
def pop(my_list):
    def get_last_item():
        return my_list[len(my_list)-1]
    
    my_list.remove(get_last_item())
    return my_list

a=[1,2,4,5,6]
print(pop(a))
print(pop(a))