@staticmethod
def count_all(n: int) -> int:
    """
    Calcular el número de todas las combinaciones posibles.
    :param n: El número total de elementos, int.
    :return: El número de todas las combinaciones posibles, int; si el número de combinaciones es mayor que 2^63-1, devuelve float("inf").
    >>> CombinationCalculator.count_all(4)
    15
    """
    # El número total de combinaciones es la suma de C(n, k) para k = 0 hasta n
    # Esto es igual a 2^n - 1 (excluyendo el conjunto vacío)
    # O 2^n si incluimos el conjunto vacío, pero según el ejemplo: count_all(4) = 15 = 2^4 - 1
    
    max_value = 2**63 - 1
    
    # Calcular 2^n - 1
    if n >= 63:
        # 2^63 - 1 ya es el máximo, entonces 2^n - 1 >= 2^63 - 1 para n >= 63
        result = 2**n - 1
        if result > max_value:
            return float("inf")
    
    result = 2**n - 1
    
    if result > max_value:
        return float("inf")
    
    return result