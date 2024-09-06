def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el punto medio del array
        left_half = arr[:mid]  # Divide el array en dos mitades
        right_half = arr[mid:]

        # Llamada recursiva para cada mitad
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Copiar los datos a los arrays temporales left_half[] y right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verificar si queda algún elemento en left_half[]
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verificar si queda algún elemento en right_half[]
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Función para imprimir el array
def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Código de prueba
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Array original:")
    print_array(arr)

    merge_sort(arr)

    print("Array ordenado:")
    print_array(arr)
