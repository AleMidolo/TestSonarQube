def gaussian(x):
    """
    गौसियन 0.1 के सिग्मा के साथ 0.2 के आसपास केन्द्रित है।
    """
    import math
    mu = 0.2  # Mean (center)
    sigma = 0.1  # Standard deviation
    
    # Gaussian function formula
    return (1.0 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(x - mu)**2 / (2 * sigma**2))