from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
my_list2 = [2,2,2,2]

odd = [i for i in my_list if (i % 2 != 0)]
odd2 = list(filter(lambda x: x%2 != 0, my_list))
odd3 = list(map(lambda x: x**2, my_list))
odd4 = reduce(lambda a, b: a * b, my_list2)

print(odd)
print(odd2)
print(odd3)
print(odd4)


