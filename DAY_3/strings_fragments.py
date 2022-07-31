miTexto = "ABCDEFGHIJKLMNOPQRSTUVWYZ"

fragmento = miTexto[0:10] # el primer valor indica donde empieza, el segundo hasta donde
print("El fragmento extraido es: " + fragmento)

fragmento = miTexto[0:10:2] # el tercer valor indica la frecuencia con la que coge dato, en este caso, de dos en dos
print("El fragmento extraido es: " + fragmento)

fragmento = miTexto[::-1] # Con esto le damos la vuelta al string
print("El fragmento extraido es: " + fragmento)