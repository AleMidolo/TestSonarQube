def count(n: int, m: int) -> int:
    """
    Calcula el número de combinaciones para un conteo específico.
    :param n: El número total de elementos, int.
    :param m: El número de elementos en cada combinación, int.
    :return: El número de combinaciones, int.
    >>> CombinationCalculator.count(4, 2)
    6
    """
    if m > n or m < 0 or n < 0:
        return 0
    
    if m == 0 or m == n:
        return 1
    
    # Calculate factorial
    def factorial(num):
        if num <= 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
    
    # C(n, m) = n! / (m! * (n - m)!)
    return factorial(n) // (factorial(m) * factorial(n - m))