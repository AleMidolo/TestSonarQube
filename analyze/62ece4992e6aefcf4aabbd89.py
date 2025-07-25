import numpy as np

def gaussian(x):
    """
    Calcular la Gaussiana centrada en u = 0.2 y sigma = 0.1.  
    """
    u = 0.2
    sigma = 0.1
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - u) / sigma) ** 2)