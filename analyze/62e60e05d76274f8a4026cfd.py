def index(self, key):
    """
    Return the index of the given item.

    :param key: a key
    :return: index
    :rtype: int
    """
    for i, item in enumerate(self):
        if item == key:
            return i
    raise ValueError(f"{key} is not in the list")