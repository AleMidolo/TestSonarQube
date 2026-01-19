def taylor(self, x, n):
    """
    Trova il valore dell'espansione di Taylor di n-esimo ordine di cos (x/180 * pi)
    :param x: int
    :param n: int
    :return: float
    >>> tricalculator.taylor(60, 50)
    0.5000000000000001
    """
    import math
    
    # Convert x from degrees to radians
    x_rad = x / 180 * math.pi
    
    # Taylor series for cos(x) around 0:
    # cos(x) = sum from k=0 to n of: (-1)^k * x^(2k) / (2k)!
    result = 0.0
    
    for k in range(n + 1):
        term = ((-1) ** k) * (x_rad ** (2 * k)) / math.factorial(2 * k)
        result += term
    
    return result