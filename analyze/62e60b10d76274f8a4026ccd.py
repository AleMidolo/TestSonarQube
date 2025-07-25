def data(self, *keys):
    # If no keys provided, return all data
    if not keys:
        return dict(zip(self._fields, self))
    
    result = {}
    
    # Process each key
    for key in keys:
        try:
            # If key is integer, treat as index
            if isinstance(key, int):
                if key >= len(self):
                    raise IndexError(f"Index {key} is out of range")
                result[self._fields[key]] = self[key]
            # If key is string, treat as field name    
            else:
                try:
                    index = self._fields.index(key)
                    result[key] = self[index]
                except ValueError:
                    result[key] = None
        except IndexError:
            raise IndexError(f"Index {key} is out of range")
            
    return result