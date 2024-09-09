immutable_var = tuple ([1,2,'a','b'])
print(immutable_var)
# immutable_var [0] = 10
# print(immutable_var)
# значение элементов не изменится, потому что строковые и числовые элементы неизменяемые, можно изменить только если в кортеже находится список элементов
mutable_list = tuple ([[1,2,'a','b']])
mutable_list [0][1] = 3
mutable_list [0][3] = 'New'
print(mutable_list)
