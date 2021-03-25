with open(r"C:\\Users\\1333156\Scripts\work\\test\\File_handling\demo.txt",'r') as fp:
    print(fp.read())
    print(fp.read(9))
fp.close()

fh = open(r"C:\\Users\\1333156\Scripts\work\\test\\File_handling\demo.txt",'r')
print(fh.read(5))
print(fh.readline())
print(fh.readline())
fh.close()

fi = open(r"C:\\Users\\1333156\Scripts\work\\test\\File_handling\demo.txt",'r')
print(fi.readlines()) #returns a list 
fi.close()