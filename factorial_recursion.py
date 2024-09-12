def factorial(n):
    # Caso base: El factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * factorial de (n-1)
    else:
        return n * factorial(n - 1)


# Ejemplo de uso:
print(factorial(5))  # Esto devolverá 120, ya que 5! = 5 * 4 * 3 * 2 * 1
