promedio, sum, contar = 0.0, 0, 0
promedio = 0.0
sum = 0
contar = 0
print("Introduzca la nota de un estudiante (-1 para salir):")
nota = int(input())
#se va a realizar cuando sea verdero
while nota != -1:
   sum = sum + nota
   contar = contar + 1
   print("Introduzca la nota del estudiante (-1 para salir):")
   nota = int(input())
#cuando sea falso
promedio = sum / contar
print("El promedio del alumno es ", promedio)