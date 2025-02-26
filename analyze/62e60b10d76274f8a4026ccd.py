def data(self, *keys):
    """
    Return the keys and values of this record as a dictionary,
    optionally including only certain values by index or key. Keys
    provided in the items that are not in the record will be
    inserted with a value of :const:`None`; indexes provided
    that are out of bounds will trigger an :exc:`IndexError`.

    :param keys: indexes or keys of the items to include; if none
                  are provided, all values will be included
    :return: dictionary of values, keyed by field name
    :raises: :exc:`IndexError` if an out-of-bounds index is specified
    """
    if not keys:
        return {key: getattr(self, key, None) for key in self.__dict__}

    result = {}
    for key in keys:
        if isinstance(key, int):
            if key < 0 or key >= len(self.__dict__):
                raise IndexError("Index out of bounds")
            key_name = list(self.__dict__.keys())[key]
            result[key_name] = self.__dict__.get(key_name, None)
        else:
            result[key] = getattr(self, key, None)

    return result