def data(self, *keys):
    result = {}
    record_keys = list(self.__dict__.keys())
    
    for key in keys:
        if isinstance(key, int):
            if key < 0 or key >= len(record_keys):
                raise IndexError("Index out of bounds")
            result[record_keys[key]] = self.__dict__.get(record_keys[key], None)
        else:
            result[key] = self.__dict__.get(key, None)
    
    if not keys:
        return self.__dict__
    
    return result