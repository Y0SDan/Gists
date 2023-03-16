import random

# Crear un archivo vacío llamado numeros.txt
archivo = open("numeros.txt", "w")

# Generar 100000 numeros aleatorios entre 1 y 1000
for i in range(100000):
    numero = random.randint(1, 1000)
    # Escribir el numero en el archivo seguido de un espacio
    archivo.write(str(numero) + " ")

# Cerrar el archivo
archivo.close()