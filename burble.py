def bubble_sort(arr):
    n = len(arr)
    # Iteramos a través de todos los elementos del arreglo
    for i in range(n):
        # Last i elementos ya están ordenados
        for j in range(0, n-i-1):
            # Iteramos a través del arreglo desde 0 hasta n-i-1
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Pedimos al usuario ingresar 5 números
numeros = []
for i in range(5):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

# Imprimimos el arreglo original
print("Arreglo original:", numeros)

# Ordenamos el arreglo con el algoritmo burbuja
bubble_sort(numeros)

# Imprimimos el arreglo ordenado
print("Arreglo ordenado:", numeros)
