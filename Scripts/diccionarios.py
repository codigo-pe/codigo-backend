#manejo de diccionarios
cursos = {'python':500,'flask':800,'django':900}
#imprimir solo un valor del diccionario
print(cursos['django'])
#otra forma de hacer lo mismo - get es traer el valor segun la clave
print(cursos.get('django'))
#imprimir todos los elementos del diccionario
print(cursos)
#añadir un elemento al diccionario
#si no lo encuentra lo inserta sino lo sobreescribe
cursos['node']=750
print(cursos)
#eliminar un valor del diccionario
del cursos['python']
print(cursos)
#recorrer el diccionario y recuperar su clave y valor
for k,v in cursos.items():
    print(k,v)
keys=cursos.keys()
values=cursos.values()
print(keys)
print(values)