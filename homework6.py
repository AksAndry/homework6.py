#1) Работа со словарями:
my_dict = { 'Andrey': 1995, 'Igor': 1990, 'Ivan': 1985, 'Sergey': 1998}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get ('Egor'))
my_dict.update ({'Sasha': 2000, 'Vova': 2004})
print(my_dict)
my_dict.pop('Sergey')
print(my_dict)
a = my_dict.pop('Sasha')
print(a)
print(my_dict)

#2) Работа с множествами:
my_set = {1, 1, 1, 2, 2, 3, 3, 'stepler', 'stepler' ,3.14, 5, 7, 8}
print(my_set)
print(my_set.add(10))
print(my_set.add(15))
print(my_set)
print(my_set.discard (3))
print(my_set)

