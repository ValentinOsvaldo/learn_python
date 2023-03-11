# Dictionaries

empty_dict = {}
dct = {
    'key': 'value'
}

print(empty_dict)
print(dct)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(len(person))

print(person['first_name'])
print(person.get('last_name'))

# Copy a dictionary
person_copy = person.copy()

print('Person copy:', person_copy)

# Getting dictionary keys as a list
print(person.keys())

# Getting dictionary values as a list
print(person.values())

# Excercises

dog = {}

print('Dog:', dog)

dog['name'] = 'Bunny'
dog['color'] = 'white'
dog['breed'] = 'chihuahua'
dog['legs'] = 'short'
dog['age'] = 3

print('Dog:', dog)

# Use loop in dictionary
for keys in dog:
  print(keys)

new_order = {
	'name': '',
  'address': ''
}

new_order['name'] = input('Enter your name: ')
new_order['address'] = input('Enter your address: ')

print(new_order)
