def decorator_X(func):
    def wrapper_function():
        print('X'*20)
        func()
        print('X'*20)
    return wrapper_function

def decorator_Y(func):
    def wrapper_function():
        print('Y'*20)
        func()
        print('Y'*20)
    return wrapper_function

@decorator_X
@decorator_Y
def say_hello():
    print('Hello world')

say_hello()