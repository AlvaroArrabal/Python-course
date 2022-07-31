text = "Este es mi texto"

res = text.upper()
print(res)

res = text.lower()
print(res)

res = text[3].upper()
print(res)

res = text.split() # separa cada palabra (por defecto toma los espacios) en una lista
print(res)

res = text.split("e") # toma el valor como método de separación
print(res)

a = "Hola"
b = "me"
c = "llamo"
d = "Alvaro"
e = " ".join([a,b,c,d]) # IMPORTANTE: a join se le pasan 'listas' 

print(e) # como le hemos aplicado join al espacio " " separa cada palabra con eso

e = "-".join([a,b,c,d])
print(e)

res = text.find("m")
print(res)

res = text.find("j") # si la palabra no está devuelve -1
print(res)

res = text.replace("texto","ejemplo")
print(res)

res = text.replace("e","3") # reemplaza todas las letras
print(res)

frase = """Hola que tal
espero que estes
perfectamente"""
print(frase)

print("espero" in frase) # devuelve un booleano si la palabra está en el string
print("agua" in frase) # No está, devolverá flase

print("agua" not in frase) # Devuelve true si NO está en el string