#Lambda function is defined by syntax lambda <arguments>:<Operation>

def double(x):
    return x*2

def add(x,y):
    return x+y

def product(x,y,z):
    return x*y*z

double_lam = lambda x:x*2 
add_lam = lambda x,y:x+y
product_lam = lambda x,y,z:x*y*z

print(double(2),double_lam(2))
print(add(2,3),add_lam(2,3))
print(product(2,3,4),product_lam(2,3,4))
