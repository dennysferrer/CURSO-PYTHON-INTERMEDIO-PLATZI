my_list = [1,2,3,4,5,6,7,8,9,10,11,12]

my_list2 = list(filter(lambda x: x%2!=0, my_list))

print(my_list2)