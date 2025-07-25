def to_csv(self, separator=",", header=None):
    """Convert graph points to CSV format."""
    result = []
    
    # Add header if provided
    if header is not None:
        result.append(header)
        
    # Convert each point to CSV format
    for point in self:
        # Convert coordinates to string, separated by separator
        coord_str = separator.join(str(x) for x in point.coord)
        
        # Convert values to string, separated by separator 
        if hasattr(point, 'values'):
            if isinstance(point.values, (list, tuple)):
                val_str = separator.join(str(x) for x in point.values)
            else:
                val_str = str(point.values)
            
            # Combine coordinates and values
            point_str = coord_str + separator + val_str
        else:
            point_str = coord_str
            
        result.append(point_str)
        
    # Join all lines with newlines
    return "\n".join(result)