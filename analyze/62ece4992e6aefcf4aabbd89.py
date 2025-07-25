import numpy as np

def gaussian(x):
    """
    Gaussian centered around 0.2 with a sigma of 0.1.
    """
    mean = 0.2
    sigma = 0.1
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / sigma) ** 2)