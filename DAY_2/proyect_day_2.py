nombre = input("Cual es tu nombre: ")
ventas = input("Cuanto has vendido: ")

ventas = float(ventas)

print(f"Ok {nombre}. Este mes ganaste {round(ventas*0.13, 2)}")