#my_func is a generator method 

def my_func():

    for i in range(6):
        print("--------")
        yield i

def my_fun():
    for j in range(5):
        print("::::")
        print(j)
        return j 

x = my_func()
print(type(x))
y=my_fun()
print(type(y))

for i in range(6):
    print("value is ", next(x))