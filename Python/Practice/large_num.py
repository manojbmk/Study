n=[]
a=int(input("enter the no of iterations :  "))
# for i in range(1,a+1):
#     b=int(input("Enter the element : "))
#     n.append(b)

# n.sort()
# print(n,a)
# print("Largest number is : ",n[a-1])

x = 0
for i in range(a):
    b=int(input("enter the element : "))
    if b > x :
        large = b
        x = b
        print(large,x,b)
    else:
        continue
print(large)
