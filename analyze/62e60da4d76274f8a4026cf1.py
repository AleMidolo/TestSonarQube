def values(self, *keys):
    # If no keys provided, return all values
    if not keys:
        return list(self._data.values())
    
    # If keys provided, return values for those keys only
    result = []
    for key in keys:
        # Handle both index and key access
        if isinstance(key, int):
            # Get value by index
            try:
                result.append(list(self._data.values())[key])
            except IndexError:
                continue
        else:
            # Get value by key
            if key in self._data:
                result.append(self._data[key])
    
    return result