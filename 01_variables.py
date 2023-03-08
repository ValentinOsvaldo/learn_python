# Variables y funciones del sistema propio de python

my_variable = 'Esta es una variable'
my_number = 117
my_bool = True

# Concatenación de cadenas
print(my_variable, my_number, my_bool)
print(type(my_variable), type(my_number), type(my_bool))

# Declarar multiples variables en una sola linea (No abusar)
# Nota: También nos recuerda a la destructuración de JS
first_name, last_name, age = 'Osvaldo', 'Valentin', 20
print(first_name, last_name, age)

# Input
country = input('What is your country? ')
print(country)

# Metodos de python

# El .length de Python
print(len(my_variable))

# Convierte una variable diferente de string a un string
my_number = str(my_number) 
print(my_number, type(my_number))

# Otros tipos
int()
float()
bool()
list()

# Obtener el minimo y el máximo
print(max(1,2,3))
print(min(1,2,3))
