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
    if len(data) == 0:
        return None
    mean = Statistics3.mean(data)
    if mean is None:
        return None
    variance = sum(((x - mean) ** 2 for x in data)) / len(data)
    return math.sqrt(variance)