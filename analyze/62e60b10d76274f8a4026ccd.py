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
    # Assuming self._fields contains the field names and self._values contains the corresponding values
    if not hasattr(self, '_fields') or not hasattr(self, '_values'):
        raise AttributeError("Record does not have '_fields' or '_values' attributes.")
    
    result = {}
    if not keys:
        # If no keys are provided, include all fields
        for field, value in zip(self._fields, self._values):
            result[field] = value
    else:
        for key in keys:
            if isinstance(key, int):
                # Handle index-based access
                if key < 0 or key >= len(self._fields):
                    raise IndexError(f"Index {key} is out of bounds.")
                field = self._fields[key]
                result[field] = self._values[key]
            else:
                # Handle key-based access
                if key in self._fields:
                    index = self._fields.index(key)
                    result[key] = self._values[index]
                else:
                    # Insert None for keys not in the record
                    result[key] = None
    return result