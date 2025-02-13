import numpy as np

def gaussian(x):
    u = 0.2
    sigma = 0.1
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - u) / sigma) ** 2)