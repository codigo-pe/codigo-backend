promedio, sum, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir):"
#es solo para la primera vez
nota = int(input(mensaje))
while nota != -1:
   sum = sum + nota
   contar += 1
   #para n veces hasta que se ingrese -1
   nota = int(input(mensaje))
else:
   promedio = sum / contar
   print("El promedio del alumno es ", promedio)