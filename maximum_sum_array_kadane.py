def maximum_subarray_sum(arr):
    # Inicializamos max_current y max_global con el primer elemento del arreglo
    max_current = max_global = arr[0]

    # Recorremos el arreglo desde el segundo elemento
    for i in range(1, len(arr)):
        # Calculamos max_current como el mayor entre el elemento actual y la suma del subarreglo anterior
        # más el elemento actual
        max_current = max(arr[i], max_current + arr[i])

        # Actualizamos max_global si max_current es mayor
        if max_current > max_global:
            max_global = max_current

    return max_global


# Ejemplo de uso
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray_sum(arr))  # Salida: 6 (correspondiente al subarreglo [4, -1, 2, 1])
