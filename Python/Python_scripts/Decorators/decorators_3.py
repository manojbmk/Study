def decorator_divide(func):
    def wrapper_function(a,b):
        print("divide ",a,' and ',b)
        if b == 0:
            print("Division with zero is not possible")
            return 0
        return a/b
    return wrapper_function

    
@decorator_divide
def divide(x,y):
    return x/y

print(divide(10,4))
print(divide(2,0))