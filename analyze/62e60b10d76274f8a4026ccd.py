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
        # If no keys provided, return all items
        return dict(zip(self._keys, self._values))
    
    result = {}
    for key in keys:
        if isinstance(key, int):
            # Handle index access
            if key < 0:
                key = len(self._keys) + key
            if key >= len(self._keys) or key < 0:
                raise IndexError(f"Index {key} out of bounds")
            result[self._keys[key]] = self._values[key]
        else:
            # Handle key access
            try:
                index = self._keys.index(key)
                result[key] = self._values[index]
            except ValueError:
                # Key not found, set value to None
                result[key] = None
                
    return result