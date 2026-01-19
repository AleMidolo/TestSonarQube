def taylor(self, x, n):
    """
    cos (x/180 * pi) का n-आदेश टेलर विस्तार मान खोजें
    :param x: int
    :param n: int
    :return: float
    >>> tricalculator.taylor(60, 50)
    0.5000000000000001
    """
    import math
    
    # Convert degrees to radians
    angle_rad = x / 180 * math.pi
    
    # Taylor series for cos(x) = sum from k=0 to n of ((-1)^k * x^(2k)) / (2k)!
    result = 0.0
    
    for k in range(n + 1):
        term = ((-1) ** k) * (angle_rad ** (2 * k)) / math.factorial(2 * k)
        result += term
    
    return result