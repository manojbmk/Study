def func():
    global x ## By declaring in this way, the below statement executes that x is variable declared in global scope
    print(x)
    x = "kumar" ## Local scope ## The value is over-written.
    print(x)

x = "manoj"  ## Global scope ## Over written value of x is present here because global keyword is used in line 2. 
func()

print(x) 

 #_-----------------------------------------# 


def func1():
    x=50
    def inner():
        nonlocal x 
        x=100
    
    print("1-----",x)
    inner()
    print("2-----",x)

x = 20
func1()
print("3-----",x)