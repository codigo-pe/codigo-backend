import math
import urllib

print(math.pi)

import random
#cualquier número al azar
print(random.random())
#cualquier número al azar especificando el límite
print(random.randrange(5))

import statistics
datos=[20,13,45,67,89,89,12,56,789,87]
print(statistics.mode(datos))
print(statistics.median(datos))
print(statistics.variance(datos))

from datetime import date
hoy=date.today()
print(hoy)

with urllib.request.urlopen("http://wwww.codigo.edu.pe") as url:
    s=url.red()
    print(s)


from openpyxl import load_workbook
wb = load_workbook(filename="D:data.xlsx")
sheet_ranges=wb['informacion']
print(sheet_ranges['B4'].value)
