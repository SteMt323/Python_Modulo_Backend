### Type Hints ###

# Recordemos que python es un lenguaje de tipado dinámico
my_string = "Hola mundo"
print(type(my_string))

my_string = 5
print(type(my_string))
[]
"""
FastApi recomienda que declaremos las variables su "tipo",
aunque python es de tipado débil, al indicarle el tipo de dato, se le tomara como el tipo de dato indicado
"""
my_typed: str = "My typed is a string"
print(my_typed)
print(type(my_typed))

my_typed = 5 # sigue siendo un string
print(my_typed)
print(type(my_typed)) # aunque lo imprima como int, las operaciones sobre el seguiran siendo de strings