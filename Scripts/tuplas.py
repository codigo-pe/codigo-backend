back = ('python' , 'flask' , 'django')
front = ('html' , 'css' , 'javascript')
nueva = back + front
def listar_tuplas():
    for c in nueva:
        print(c)
def recorrer():
    print (nueva[:5])

#listar_tuplas()
recorrer()