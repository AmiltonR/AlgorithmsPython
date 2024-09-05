def quadratic_linear_search(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1):
            if arr[i] == target:
                return i
    return -1  # Si no se encuentra el elemento


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Compara el valor del medio con el objetivo
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Si no se encuentra el elemento


arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

# Llamada a la búsqueda cuadrática (ineficiente)
index = quadratic_linear_search(arr, target)
print(f"Element found at index (Quadratic Search): {index}")

# Llamada a la búsqueda binaria (eficiente)
index = binary_search(arr, target)
print(f"Element found at index (Binary Search): {index}")
