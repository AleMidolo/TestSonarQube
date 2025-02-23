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
    result = {}
    if not keys:
        # If no keys are provided, return all items
        for key in self.record.keys():
            result[key] = self.record.get(key, None)
    else:
        for key in keys:
            if isinstance(key, int):
                if key < 0 or key >= len(self.record):
                    raise IndexError("Index out of bounds")
                result[self.record[key]] = self.record.get(self.record[key], None)
            else:
                result[key] = self.record.get(key, None)
    return result