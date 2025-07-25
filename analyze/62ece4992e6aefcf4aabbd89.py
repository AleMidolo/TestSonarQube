def gaussian(x):
    """
    Questa funzione calcola il valore della distribuzione gaussiana per un dato `x`, con una media `u` pari a 0.2 e una deviazione standard `sigma` pari a 0.1.
    """
    import math
    
    u = 0.2  # media
    sigma = 0.1  # deviazione standard
    
    # Formula della distribuzione gaussiana
    exponent = -((x - u) ** 2) / (2 * sigma ** 2)
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    
    return coefficient * math.exp(exponent)