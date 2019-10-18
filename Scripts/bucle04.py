nalumnos=int(input("cuántos alumnos son?"))
notas = 0
sum = 0
for i in range(nalumnos):
    notas = int(input("Ingresar Nota" + str(i) + " "))
    sum = sum + notas
promedio = sum / (i + 1)
print("El promedio es: " + str(promedio))
if promedio > 10.5:
    print("Aprobo el curso")
else:
    print("No llegó a Aprobar")