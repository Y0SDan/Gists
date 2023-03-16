# Abrir el archivo y leer los números
with open('numeros.txt', 'r') as file:
    numeros = list(map(int, file.read().split()))

# Pedir al usuario el número a buscar
num_buscar = int(input("Ingresa el número que deseas buscar: "))

# Buscar el número en la lista
indices = [i for i, x in enumerate(numeros) if x == num_buscar]

if len(indices) == 0:
    print(f"El número {num_buscar} no se encuentra en el archivo.")
else:
    print(f"El número {num_buscar} se encuentra en el archivo {len(indices)} veces.")

    # Mostrar las posiciones en las que se encuentra el número
    print("Posiciones:")
    for i in indices:
        print(f"{i+1}: {numeros[i]}")