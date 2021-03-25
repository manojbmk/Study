def factorial(num):
    if num < 0:
        print("Invalid number")
        exit(1)
    elif num == 1 or 0:
        return 1
    else:
        return num*factorial(num-1)

num=int(input("enter the number : "))
print("Factorial of {} is {} ".format(num,factorial(num)))
