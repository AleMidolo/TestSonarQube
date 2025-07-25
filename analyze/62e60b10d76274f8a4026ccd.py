def data(self, *keys):
    # If no keys provided, return all fields
    if not keys:
        return dict(zip(self._fields, self))
        
    # Initialize result dictionary
    result = {}
    
    # Process each requested key
    for key in keys:
        try:
            # Handle numeric index
            if isinstance(key, int):
                if 0 <= key < len(self):
                    result[self._fields[key]] = self[key]
                else:
                    raise IndexError(f"Index {key} is out of range")
            # Handle string field name
            else:
                try:
                    index = self._fields.index(key)
                    result[key] = self[index]
                except ValueError:
                    result[key] = None
                    
        except IndexError:
            raise IndexError(f"Index {key} is out of range")
            
    return result