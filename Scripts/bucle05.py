lista = []
for i in range(9):
    palabra = input("ingrese palabra: ")
    lista.append(palabra)
keyword = input("qué textp desea buscar? ")
encontrado = False
for i in range(9):
    if keyword == lista[i-1]:
        encontrado = True
if encontrado == True:
    print("el texto fue encontrado")
else:
    print("el texto no fue encontrado")
#el profesor resolvió el ejercicio utilizando el método count para las listas.
