#One way of decorators
def decorator_func(func):
    def wrapper_function():
        print('X'*20)
        func()
        print('Y'*20)
    return wrapper_function

def say_hello():
    print('Hello world')


hello = decorator_func(say_hello)
hello()


#Second way of decorators
def decorator_func(func):
    def wrapper_function():
        print('X'*20)
        func()
        print('Y'*20)
    return wrapper_function

@decorator_func
def say_hello():
    print('Hello world')

say_hello()