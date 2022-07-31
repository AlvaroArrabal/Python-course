def reducir_lista(lista):
    lista.sort()
    lista_nueva=[]

    for i in lista:
        if i not in lista_nueva:
            lista_nueva.append(i)
    
    
    return lista_nueva



def promedio(lista):
    suma = 0

    for i in lista:
        suma += i
    
    media = suma / len(lista)

    return media



lista = [5,4,3,7,1,8,9,3,4,6,2,4,2,3,7,9,5,4,3]

lista_corta = [1,2,15,7,2,8]

print(reducir_lista(lista_corta))

