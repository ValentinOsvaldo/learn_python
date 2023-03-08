# STRINGS

my_strings = 'Mision: salvar el mundo'
my_other_strings = 'Mision completada'

print(len(my_strings))
print(my_strings + ' | ' + my_other_strings)

multiline_string = 'Esta es una línea\nEsta es otra línea'
print(multiline_string)

tab_string = '\tEste es un string con tab'
print(tab_string)

## Formateo

name, last_name, age = 'Vanessa', 'Díaz', 20

print('Mi nombres es %s %s y tengo %s años'%(name, last_name, age))
print('Mi nombres es {} {} y tengo {} años'.format(name, last_name, age))
# Este es el metodo mejor
print(f'Mi nombres es {name} {last_name} y tengo {age} años')

## Desempaquetado de caracteres
language = 'python'
a, b, c, d, e, f = language

print(a, b, c, d, e, f)

print(language[0])
print(language[-1]) # If we want to start from right end we can use negative indexing. -1 is the last index. Expected output 'n'

# In python we can slice strings into substrings.
print(language[0:3]) # Expected Output: Pyt

# Reversing a String
print(language[::-1]) # Expected output: nohtyP

# Skipping Characters While Slicing
print(language[0:6:2]) # Expected output: Pto

## Metodos

print(language.capitalize())
print(language.upper())
print(language.lower())

print( '   Colin Django   ' )

print( '   Colin Django   '.strip() )

print( 'Colin Django'.join('Osva') )

print( ('Colin Django') )

print( ''.join(list('Colin Django')) )
