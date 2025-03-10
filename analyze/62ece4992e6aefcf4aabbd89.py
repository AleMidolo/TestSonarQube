import math

def gaussiana(x):
    """
    Questa funzione calcola il valore della distribuzione gaussiana per un dato `x`, con una media `u` pari a 0.2 e una deviazione standard `sigma` pari a 0.1.
    """
    u = 0.2
    sigma = 0.1
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -((x - u) ** 2) / (2 * sigma ** 2))
    return coefficient * math.exp(exponent)