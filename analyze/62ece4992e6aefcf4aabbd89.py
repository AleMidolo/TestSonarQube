import math

def gaussian(x):
    """
    Calcular la Gaussiana centrada en u = 0.2 y sigma = 0.1.
    
    Parameters:
    x (float): El valor en el que se evalúa la función Gaussiana.
    
    Returns:
    float: El valor de la función Gaussiana en x.
    """
    u = 0.2
    sigma = 0.1
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - u) ** 2) / (2 * sigma ** 2))