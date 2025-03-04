def data(self, *keys):
    if not keys:
        # If no keys specified, return all fields
        return dict(zip(self.keys(), self.values()))
    
    result = {}
    for key in keys:
        try:
            if isinstance(key, int):
                # Handle numeric index
                field_name = self.keys()[key]
                result[field_name] = self.values()[key]
            else:
                # Handle field name
                result[key] = self[key] if key in self else None
        except IndexError:
            raise IndexError("Index out of bounds")
            
    return result