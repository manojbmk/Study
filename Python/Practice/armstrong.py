from sample import * 

for i in n:
    sum1=0
    tmp = i
    while i > 0:
        rem = i%10
        sum1=sum1+rem**3
        i=i//10 
    if sum1 == tmp:
        print(tmp, " is a armstrong number")
    else:
        print(tmp," is not a armstrong number")