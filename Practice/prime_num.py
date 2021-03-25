num = int(input("Enter the number:  "))

if num > 1:
    for i in range(2,round(num/2)):
        if num%i == 0:
            print(num," is not a prime number")
            break
    else:
        print("{} is a prime number".format(num))
else:
    print(num," is Not a Prime number")
