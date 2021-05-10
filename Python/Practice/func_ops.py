def first(a):
    print(a)

def second(a,b):
    print(a)
    print(b)

def third(*args1):
    print(args1)
    sum=0
    for x in args1:
        sum = sum+x
    print(sum)

first(1)
second(b=2,a=4)
third(3,65,5)

