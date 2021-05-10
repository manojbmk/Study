length = int(input("Enter range : "))

for i in range(2,length+1):
    count = 0
    for j in range(1,(i//2)+1):
        if i%j == 0:
            count=count+1
    if count == 1:
        print(i)
