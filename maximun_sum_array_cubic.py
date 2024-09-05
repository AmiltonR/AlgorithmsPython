def maximum_subarray_sum(arr):
    n = len(arr)
    max_sum = float('-inf')  # Inicializamos con el valor más pequeño posible

    # Iteramos sobre todos los subarreglos posibles
    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            # Calculamos la suma del subarreglo desde i hasta j
            for k in range(i, j + 1):
                current_sum += arr[k]
            # Actualizamos max_sum si encontramos una suma mayor
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


# Ejemplo de uso
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray_sum(arr))  # Salida: 6 (correspondiente al subarreglo [4, -1, 2, 1])
