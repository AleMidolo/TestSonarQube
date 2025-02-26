def gaussian(x):
    """
    Calcular la Gaussiana centrada en u = 0.2 y sigma = 0.1.  
    """
    import math
    u = 0.2
    sigma = 0.1
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -((x - u) ** 2) / (2 * sigma ** 2)
    return coefficient * math.exp(exponent)