from sample import * 

for i in n:
    sum1  = 0
    tmp = 1 
    while tmp <= i/2:
        if i%tmp == 0:
            sum1 = sum1+tmp
        tmp =tmp+1
    if i == sum1:
        print(i, " is a perfect number")
    else:
        print(i," is not a perfect number")
        


