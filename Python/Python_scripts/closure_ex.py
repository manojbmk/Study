def outerFunction(text):
    def innerFunction(): ##InnerFunction is a closure function as it is able to text value which is stored outside of it. 
        print(text)
    return innerFunction

a = outerFunction("Hello") #Now 'a' is innerFunction variable
a()
del outerFunction
a()

##Example 2 
def nth_power(exponent):
    def base_power(base):
        return base**exponent
    return base_power

b = nth_power(4)
print(b(3))
del nth_power
print(b(3))