my_dict= {'Natali':1990, 'Kat':1991,'Yulia': 1992}
print(my_dict)
print(my_dict['Kat'])
print(my_dict.get('Den'),'Увы, такого ключа нет')
my_dict.update ({'Den':2001,
                 'Nikita':1996})
a = my_dict.pop('Yulia')
print(a)
print(my_dict)
my_set={5,10,5,10,'omlet',False, 'omlet'}
print(my_set)
list_= {2,3}
print(my_set|set(list_))
my_set.remove(5)
print(my_set|set(list_))