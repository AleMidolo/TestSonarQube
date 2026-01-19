@staticmethod
def correlation(x, y):
    """
    दो दी गई लिस्ट का कोरिलेशन कैलकुलेट करता है।

    :param x: list, पहली लिस्ट
    :param y: list, दूसरी लिस्ट
    :return: float, दोनों लिस्ट का कोरिलेशन

    >>> statistics3 = Statistics3()
    >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
    1.0
    """
    if len(x) != len(y) or len(x) == 0:
        raise ValueError("Lists must have the same non-zero length")
    
    n = len(x)
    
    # Calculate means
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # Calculate numerator (covariance)
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    
    # Calculate denominator (product of standard deviations)
    sum_sq_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    sum_sq_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    
    denominator = (sum_sq_x * sum_sq_y) ** 0.5
    
    if denominator == 0:
        return 0.0
    
    return numerator / denominator