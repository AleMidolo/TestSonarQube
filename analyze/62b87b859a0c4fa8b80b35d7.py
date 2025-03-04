def to_csv(self, separator=",", header=None):
    result = []
    
    # Add header if provided
    if header is not None:
        result.append(str(header))
    
    # Convert each point to CSV format
    for point in self:
        # Convert coordinates to string, separated by separator
        coord_str = separator.join(str(x) for x in point.coord)
        
        # Convert values to string, separated by separator 
        if hasattr(point.value, '__iter__') and not isinstance(point.value, str):
            value_str = separator.join(str(x) for x in point.value)
        else:
            value_str = str(point.value)
            
        # Combine coordinate and value strings
        point_str = separator.join([coord_str, value_str])
        result.append(point_str)
        
    # Join all lines with newlines
    return '\n'.join(result)