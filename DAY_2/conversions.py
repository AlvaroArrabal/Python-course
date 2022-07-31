num1 = 20
num2 = 30.5

print(type(num1))  # para mostrar el tipo de la variable
print(type(num2))

num1 = num1 = num2


print(type(num1)) # conversión implicita, el propio python transforma para poder operar

num3 = 5.8

print(type(num3))

num4 = int(num3) # conversión explicita, es una conversión que defino yo, al pasar de un float a int se trunca

print (num4)
print(type(num4))

# Ejemplo
print("-------------------------\nEjemplo")
edad = input("Dime tu edad ")

print(type(edad))
edad = int(edad)

print(type(edad))
nueva_edad = edad + 1

print("Vas a cumplir " + str(nueva_edad)) # el print intenta concatenar un str con un int, hay que realizar la conversión del int a str para poder mostrarlo

num1 = "7.5"
num2 = "10"

num1 = float(num1)
num2 = float(num2)
print(num1 + num2)

# Redondeo

num1 = 5.86
print(round(num1,1)) # primer parámetro, es lo que quiero redondear, el segundo parámetro es el índice, si no se pone nada redondea al entero más próximo

num1 = 5.8666666666666666
print(round(num1))