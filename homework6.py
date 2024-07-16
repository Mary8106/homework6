my_dict = {'Иванов': 1981, 'Петров': 2002, 'Сидоров': 1993}
print(my_dict)
print(my_dict.get('Иванов'), my_dict.get('Крылов'))
my_dict.update({'Булдаков': 1952, 'Черных': 1964})
a = my_dict.pop('Иванов')
print (a)
print(my_dict)
my_set = {1,2,3,4,5,3,2,1}
print(my_set)
my_set.update([6,7])
my_set.discard(2)
print(my_set)
