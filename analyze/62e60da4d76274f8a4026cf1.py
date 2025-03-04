def values(self, *keys):
    """
    Return the values of the record, optionally filtering to
    include only certain values by index or key.

    :param keys: indexes or keys of the items to include; if none
                 are provided, all values will be included
    :return: list of values
    :rtype: list
    """
    if not keys:
        # If no keys specified, return all values
        return list(self._values)
    
    result = []
    for key in keys:
        if isinstance(key, int):
            # If key is integer, treat as index
            result.append(self._values[key])
        else:
            # Otherwise treat as dictionary key
            try:
                index = self._fields.index(key)
                result.append(self._values[index])
            except ValueError:
                raise KeyError(f"Field '{key}' not found")
    
    return result