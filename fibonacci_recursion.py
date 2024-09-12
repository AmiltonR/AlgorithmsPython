def fibonacci(n):
    # Caso base: Si n es 0 o 1, devolvemos n (Fibonacci(0) = 0 y Fibonacci(1) = 1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo: Fibonacci(n) es la suma de Fibonacci(n-1) y Fibonacci(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Ejemplo de uso:
print(fibonacci(5))  # Esto devolverá 5, ya que la secuencia es 0, 1, 1, 2, 3, 5
