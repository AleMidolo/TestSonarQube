@staticmethod
def z_score(data):
    """
    दिए गए सूची का z-score गणना करता है।
    :param data: दी गई सूची, सूची।
    :return: दी गई सूची का z-score, सूची।
    >>> statistics3 = Statistics3()
    >>> statistics3.z_score([1, 2, 3, 4])
    [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]

    """
    # Calculate mean
    mean = sum(data) / len(data)
    
    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    
    # Calculate z-score for each element
    z_scores = [(x - mean) / std_dev for x in data]
    
    return z_scores