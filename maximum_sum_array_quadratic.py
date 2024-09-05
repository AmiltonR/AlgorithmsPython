def maximum_subarray_sum(arr):
    n = len(arr)
    max_sum = float('-inf')  # Inicializamos con el valor más pequeño posible

    # Iteramos sobre todos los puntos de inicio del subarreglo
    for i in range(n):
        current_sum = 0
        # Sumamos elementos desde el índice i hasta el final del arreglo
        for j in range(i, n):
            current_sum += arr[j]
            # Actualizamos max_sum si encontramos una suma mayor
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


# Ejemplo de uso
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray_sum(arr))  # Salida: 6 (correspondiente al subarreglo [4, -1, 2, 1])
