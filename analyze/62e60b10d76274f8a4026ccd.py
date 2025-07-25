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
    # Assuming self._fields contains the field names and self._values contains the values
    if not keys:
        return dict(zip(self._fields, self._values))
    
    result = {}
    for key in keys:
        if isinstance(key, int):
            if key < 0 or key >= len(self._values):
                raise IndexError("Index out of bounds")
            result[self._fields[key]] = self._values[key]
        else:
            if key in self._fields:
                index = self._fields.index(key)
                result[key] = self._values[index]
            else:
                result[key] = None
    return result