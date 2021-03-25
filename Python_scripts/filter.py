my_list = [2,5,8,10,9,3.4]
my_list2 = [4,6,7,8,11,2]

c = filter(lambda x:x%2 == 0, my_list)
print(list(c))

d = filter(lambda x:True if x>5 else False, my_list2)
print(list(d))