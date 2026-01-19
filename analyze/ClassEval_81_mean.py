@staticmethod
def mean(data):
    """
    दिए गए सूची का औसत निकालता है।
    :param data: दी गई सूची, सूची।
    :return: दी गई सूची का औसत, फ्लोट।
    >>> statistics3 = Statistics3()
    >>> statistics3.mean([1, 2, 3])
    2.0

    """
    if not data:
        return 0.0
    return float(sum(data)) / len(data)