import numpy as np

def gaussian(x):
    """
    गौसियन 0.1 के सिग्मा के साथ 0.2 के आसपास केन्द्रित है।
    """
    mean = 0.2
    sigma = 0.1
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / sigma) ** 2)