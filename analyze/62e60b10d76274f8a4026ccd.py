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
    record_dict = {}
    if not keys:
        # If no keys are provided, return all items
        for key in self.__dict__:
            record_dict[key] = self.__dict__[key]
    else:
        for key in keys:
            if isinstance(key, int):
                # Handle index access
                if key < 0 or key >= len(self.__dict__):
                    raise IndexError("Index out of bounds")
                record_dict[list(self.__dict__.keys())[key]] = self.__dict__.get(list(self.__dict__.keys())[key], None)
            else:
                # Handle key access
                record_dict[key] = self.__dict__.get(key, None)
    return record_dict