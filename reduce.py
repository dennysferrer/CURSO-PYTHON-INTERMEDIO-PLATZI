from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]

total = reduce(lambda a,b : a*b, my_list)

print(total)