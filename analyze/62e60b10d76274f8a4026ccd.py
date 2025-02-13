def data(self, *keys):
    record_dict = {key: self.record.get(key, None) for key in keys} if keys else self.record.copy()
    for index in keys:
        if isinstance(index, int):
            if index < 0 or index >= len(self.record):
                raise IndexError("Index out of bounds")
    return record_dict