@staticmethod
def count_all(n: int) -> int:
    """
    Calcular el número de todas las combinaciones posibles.
    :param n: El número total de elementos, int.
    :return: El número de todas las combinaciones posibles, int; si el número de combinaciones es mayor que 2^63-1, devuelve float("inf").
    >>> CombinationCalculator.count_all(4)
    15
    """
    # El número total de combinaciones es la suma de C(n, k) para k = 1 hasta n
    # Esto es equivalente a 2^n - 1 (excluyendo el conjunto vacío)
    
    max_value = 2**63 - 1
    
    # Calcular 2^n - 1
    total = 2**n - 1
    
    # Verificar si excede el límite
    if total > max_value:
        return float("inf")
    
    return total