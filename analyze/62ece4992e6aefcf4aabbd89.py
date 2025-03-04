def gaussian(x):
    """
    Questa funzione calcola il valore della distribuzione gaussiana per un dato `x`, con una media `u` pari a 0.2 e una deviazione standard `sigma` pari a 0.1.
    """
    import math
    u = 0.2
    sigma = 0.1
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = math.exp(-0.5 * ((x - u) / sigma) ** 2)
    return coefficient * exponent