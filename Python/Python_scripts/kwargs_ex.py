def adding(name,age,**marks):
    print("name", name)
    print("age",age)
    for i,j in marks.items():
        print(i, ' ', j)
    #print("marks",marks

adding(4,5,eng=7,math=8,tel=8,hin=9,soc=9,sci=9,gk=0,cpm=3,ldic=4,ac=6)