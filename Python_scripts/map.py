#Map example-1
my_list = [2,5,8,10,9,3.4]

result = map(lambda x:x*2,my_list)

print(list(result))

#Map example-2
my_list = [2,5,8,10,9,3.4]
my_list2 = [4,6,7,8,11,2,45]

a = map(lambda x:x*2,my_list)
b = map(lambda x,y:x+y,my_list2,my_list)

print(list(a))
print(list(b))