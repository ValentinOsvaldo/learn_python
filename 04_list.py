# LIST

# DECLARE A LIST
my_list = list()
my_other_list = ['Apple', 'Lemon']

print(my_list)
print(my_other_list)

print(my_other_list[0])
print(my_other_list[-1])

things = [1, 'Hello Python', [1, 2, 3], { 'name': 'Osvaldo' }, True]

print(things)
print('Size:', len(things))

number, *rest = things

print(number) # 1
print(rest) # ['Hello Python', [1, 2, 3], {'name': 'Osvaldo'}, True]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[0:5]) # 1, 2, 3, 4, 5
