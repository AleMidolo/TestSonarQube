@staticmethod
def standard_deviation(data):
    """
    दिए गए सूची का मानक विचलन की गणना करता है।
    :param data: दी गई सूची, सूची।
    :return: दी गई सूची का मानक विचलन, फ्लोट।
    >>> statistics3 = Statistics3()
    >>> statistics3.standard_deviation([1, 2, 3])
    1.0

    """
    n = len(data)
    if n == 0:
        return 0.0
    
    # Calculate mean
    mean = sum(data) / n
    
    # Calculate variance (sum of squared differences from mean)
    variance = sum((x - mean) ** 2 for x in data) / n
    
    # Standard deviation is square root of variance
    return variance ** 0.5