miTexto = "hola me llamo alvaro y esta es una prueba"

resultado = miTexto[3]
print("resultado = " + resultado)

resultado = miTexto[-3]
print("resultado = " + resultado)

resultado = miTexto.index("a") # te muestra solo la primera coincidencia
print("resultado = " + str(resultado))

resultado = miTexto.index("a", 5) # te muestra la primera coincidencia a partir del indice que se ha introducido en la función
print("resultado = " + str(resultado))

resultado = miTexto.index("alvaro") # también se pueden buscar palabras enteras
print("resultado = " + str(resultado))

resultado = miTexto.rindex("a")
print("resultado = " + str(resultado))