my_dict = {'Anton': 1981, 'Dima': 1983, 'Pavel': 1982}
print(my_dict)
print(my_dict.get('Anton'))
print(my_dict.get('Maria'))
my_dict.update({'Lena': 1981,'Ira': 1983})
# print(my_dict.pop('Pavel') можно таким способом решить задание
x = my_dict.pop('Pavel')
print(x)
print(my_dict)
my_set = {1,1,2,3,4,2,3,(2,1),'Old','Dad','Dad','Mom','Mom',True}
print(my_set)
my_set.add(5)
my_set.add('Son')
my_set.discard('Old')
print(my_set)