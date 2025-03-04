def to_csv(self, separator=",", header=None):
    result = []
    
    # Add header if provided
    if header is not None:
        result.append(str(header))
    
    # Convert each point to CSV format
    for point in self:
        # Convert coordinates to string, separated by separator
        coord_str = separator.join(str(x) for x in point.coords)
        
        # Convert values to string, separated by separator 
        if hasattr(point, 'values'):
            values_str = separator.join(str(x) for x in point.values)
            # Combine coordinates and values
            point_str = separator.join([coord_str, values_str])
        else:
            point_str = coord_str
            
        result.append(point_str)
    
    # Join all lines with newlines
    return "\n".join(result)