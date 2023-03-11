# LIST

# DECLARE A LIST
my_list = list()
my_other_list = ['Apple', 'Lemon']

print(my_list)
print(my_other_list)

# Get length from list
print(len(my_other_list))

# get the first element
print(my_other_list[0])

# Get the last element of the list
print(my_other_list[-1])

things = [1, 'Hello Python', [1, 2, 3], {'name': 'Osvaldo'}, True]

print(things)
print('Size:', len(things))

number, *rest = things

print(number)  # 1
print('Rest:', rest)  # ['Hello Python', [1, 2, 3], {'name': 'Osvaldo'}, True]

numbers = [1, 2, 3, 4, 5]

print(numbers[0:3])  # 1, 2, 3, 4, 5

disorder_numbers = [10, 6, 8, 9, 7]
disorder_numbers.sort()

print(disorder_numbers)

# Joininig lists

new_list = numbers + disorder_numbers
print(new_list)

numbers.extend(disorder_numbers)
print(numbers)

# ? Excercise #1

# Declare an empty list
osvaldo_list = []
# Declare a list with more than 5 items
osvaldo_list = ['Halo', 'GTA', 'Minecraft',
                'Left 4 Dead', 'Star Wars: Battlefront 2']

# Find the length of your list
print(len(osvaldo_list))

# Get the first item, the middle item and the last item of the list
print(osvaldo_list[::2])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Osvaldo', 20, 1.85, 'Single', {
    'country': 'MX', 'state': 'Nuevo León', 'city': 'San Nicolas de los Garza'}]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print('Companies:', it_companies)
# Print the number of companies in the list
print('Companies list length: ', len(it_companies))
# Print the first, middle and last company
print('the first, middle and last company:', it_companies[::3])

# Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print('Edited list:', it_companies)

# Add an IT company to it_companies
it_companies.append('Intel')
print('An item added:', it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies) / 2), 'Nvidia')
print('An item added in middle:', it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# Check if a certain company exists in the it_companies list.
does_exist = 'Amazon' in it_companies
print('Is there amazon on the list?', does_exist)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three_companies = it_companies[0:3]
print(first_three_companies)

# Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print(last_three_companies)

# Slice out the middle IT company or companies from the list
middle_companies = len(it_companies) // 2
list_without_middle = it_companies[0:middle_companies] + it_companies[middle_companies + 1:]
print(list_without_middle)

# Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# Remove the middle IT company or companies from the list
middle_companies = len(it_companies) // 2
del it_companies[middle_companies]
print(it_companies)

# Remove the last IT company from the list
del it_companies[-1]
print(it_companies)

# Remove all IT companies from the list
# del it_companies[0:len(it_companies)]
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
# it_companies.clear()
del it_companies

"""
26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

tech_stack = front_end + back_end

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

new_tech_stack = tech_stack.copy()

new_tech_stack.insert(5, 'Python')
new_tech_stack.insert(6, 'SQL')

print(new_tech_stack)

# ? Exercises: Level 2

"""
1. The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
"""

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print('before:', ages)
min, *rest, max = ages
print(min, max)

# Add the min age and the max age again to the list
rest.insert(0, min)
rest.insert(len(rest), max)
print(rest)

# Find the median age (one middle item or two middle items divided by two)
median_age = len(ages) // 2
print(median_age)

# Find the average age (sum of all items divided by their number )
average_age = sum(ages, 0) / len(ages)
print(average_age)

# Find the range of the ages (max minus min)
range_age = max - min
print(range_age)

# Compare the value of (min - average) and (max - average), use abs() method
print(abs((min - average_age)))
print(abs((max - average_age)))
