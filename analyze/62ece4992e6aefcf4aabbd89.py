def gaussian(x):
    """
    Gaussian centered around 0.2 with a sigma of 0.1.
    """
    import numpy as np
    mu = 0.2  # center
    sigma = 0.1  # standard deviation
    return np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))