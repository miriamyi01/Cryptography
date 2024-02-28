#Reyes Mendoza Miriam Guadalupe
#Criptografía - Grupo 2
#Semestre 2024-2
#Facultad de Ingeniería
#Universidad Nacional Autónoma de México

#00 - PRUEBA

import fileinput

# Crear una lista vacía para almacenar las líneas de entrada
lines = []
# Leer cada línea de la entrada estándar
for line in fileinput.input():
    # Agregar cada línea a la lista
    lines.append(line)

# Inicializar una variable para almacenar la suma total
total = 0.0

# Iterar sobre cada línea en la lista de líneas
for line in lines:
    
    # Convertir la línea a un número flotante
    number = float(line)
    
    # Si el número es un entero, convertirlo a int
    if number.is_integer():
        number = int(number)
    
    # Agregar el número a la suma total
    total += number

# Si la suma total es un entero, convertirla a int
if total.is_integer():
    total = int(total)

# Imprimir la suma total
print(total)