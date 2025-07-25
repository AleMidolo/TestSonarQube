def data(self, *keys):
    if not keys:
        # If no keys specified, return all fields
        return dict(zip(self.keys(), self.values()))
    
    result = {}
    for key in keys:
        if isinstance(key, int):
            # Handle numeric index
            try:
                field_name = self.keys()[key]
                result[field_name] = self.values()[key]
            except IndexError:
                raise IndexError(f"Index {key} is out of bounds")
        else:
            # Handle field name
            result[key] = self[key] if key in self else None
            
    return result