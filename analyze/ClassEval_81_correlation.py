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
    if len(x) != len(y):
        raise ValueError('Lists must have the same length')
    if len(x) < 2:
        return None
    n = len(x)
    mean_x = Statistics3.mean(x)
    mean_y = Statistics3.mean(y)
    numerator = sum(((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)))
    denominator_x = sum(((xi - mean_x) ** 2 for xi in x))
    denominator_y = sum(((yi - mean_y) ** 2 for yi in y))
    if denominator_x == 0 or denominator_y == 0:
        return None
    return numerator / math.sqrt(denominator_x * denominator_y)