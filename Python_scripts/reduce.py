from functools import reduce

my_list = [2,5,8,10,9,3.4]
my_list2 = [4,6,7,8,11,2]

e = reduce(lambda x,y:x*y,my_list)

print(e)