def add(x,y):
    sum = x+y
    return sum 

if __name__ == "__main__":
    x = input("Enter the number : ")  
    y = input("Enter the number : ")   
    z = add(x,y)
    
    print(z)

#pdb is command used for debugging ( syntax :python -m pdb <filename>)