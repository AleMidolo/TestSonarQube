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
    
    mean_value = Statistics3.mean(data)
    std_dev = Statistics3.standard_deviation(data)
    if std_dev is None:
        return None
    z_scores = [(x - mean_value) / std_dev for x in data]
    return z_scores