# Hay varias maneras de formatear cadenas

x = 10
y = 5

print("Mis numeros son " + str(x) + " y " + str(y)) # esta sería la forma clásica, muy incómoda...

print("Mis numeros son {} y {}".format(x,y)) # esta es una de las formas mas cómodas

# también se pueden realizar operaciones
print("La suma de {} y {} es igual a {}".format(x,y,x+y))

color = "rojo"
matricula = 8292

print(f"El coche es {color} y su matricula es {matricula}") # esta es la manera más visual de hacerlo, con la 'f' antes de las "" avisamos a python que voy a mostrar variables

