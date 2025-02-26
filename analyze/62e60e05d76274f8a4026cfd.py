def index(self, key):
    """
    Return the index of the given item.

    :param key: a key
    :return: index
    :rtype: int
    """
    try:
        return self.items.index(key)
    except ValueError:
        return -1  # Return -1 if the key is not found