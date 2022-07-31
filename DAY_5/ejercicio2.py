from random import *

def lanzar_moneda():
    res = randint(0,1)
    
    if res == 0:
        return "Cara"
    else:
        return "Cruz"
        
def probar_suerte(res,lista):
    if res == "Cara":
        print("La lista se autodestruirá")
        return lista.clear()
    else:
        print("La lista fue salvada")
        return lista
    
lista_numeros=[1,2,3]

lista_numeros = probar_suerte(lanzar_moneda(),lista_numeros)

print(lista_numeros)