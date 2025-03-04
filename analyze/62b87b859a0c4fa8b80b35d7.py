def to_csv(self, separator=",", header=None):
    result = []
    
    # Add header if provided
    if header is not None:
        result.append(header)
        
    # Convert each point to CSV format
    for point in self:
        # Convert coordinates to strings separated by separator
        coord_str = separator.join(str(x) for x in point.coords)
        
        # Convert values to strings separated by separator 
        if hasattr(point.value, '__iter__'):
            val_str = separator.join(str(x) for x in point.value)
        else:
            val_str = str(point.value)
            
        # Combine coordinates and values
        row = coord_str
        if val_str:
            row += separator + val_str
            
        result.append(row)
        
    # Join rows with newlines
    return '\n'.join(result)