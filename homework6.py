my_dict={'PETG':220,'PLA':180,'Nylon':230,'Flex':210}
print(my_dict)
print(my_dict.get('PLA'))
print(my_dict.get('ABS'))
my_dict.update({'PC':290,'PEEK':360})
print(my_dict)
a=my_dict.pop('PC')
print(a)
print(my_dict)
my_set={1,'a','x',3,'a','door',True,3,2,1,'door'}
print(my_set)
my_set.add(7)
my_set.add((5,9))
my_set.discard(2)
print(my_set)





