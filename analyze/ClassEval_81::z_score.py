@staticmethod
def z_score(data):
    """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]

        """
    if len(data) < 2:
        return None
    mean_val = Statistics3.mean(data)
    std_dev = Statistics3.standard_deviation(data)
    if std_dev is None or std_dev == 0:
        return None
    z_scores = [(x - mean_val) / std_dev for x in data]
    return z_scores