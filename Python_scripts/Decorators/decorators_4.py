from time import time

def timing(func):
    def wrapper_function(*args,**kwargs):
        start = time()
        result = func(*args,**kwargs)
        stop = time()
        print("The duration of the function ", func.__name__ ," execution is ",stop-start)
        return result
    return wrapper_function
        

@timing
def my_func(num):
    total = 0 
    for i in range(num+1):
        total = total+i
    return total

print(my_func(5000000))