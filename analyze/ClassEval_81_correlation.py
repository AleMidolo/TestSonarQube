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
        raise ValueError('Lists must be of the same length.')
    mean_x = Statistics3.mean(x)
    mean_y = Statistics3.mean(y)
    numerator = sum(((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))))
    denominator = math.sqrt(sum(((x[i] - mean_x) ** 2 for i in range(len(x)))) * sum(((y[i] - mean_y) ** 2 for i in range(len(y)))))
    if denominator == 0:
        return 0
    return numerator / denominator