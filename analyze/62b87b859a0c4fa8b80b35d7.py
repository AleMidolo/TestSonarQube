def to_csv(self, separator=",", header=None):
    # Start with header if provided
    result = []
    if header is not None:
        result.append(str(header))
    
    # Convert each point to CSV format
    for point in self.points:
        # Convert coordinate to string, splitting multi-dimensional coordinates
        if isinstance(point.coordinate, (list, tuple)):
            coord_str = separator.join(str(x) for x in point.coordinate)
        else:
            coord_str = str(point.coordinate)
            
        # Convert value to string, splitting multi-dimensional values
        if isinstance(point.value, (list, tuple)):
            value_str = separator.join(str(x) for x in point.value)
        else:
            value_str = str(point.value)
            
        # Combine coordinate and value
        row = coord_str + separator + value_str
        result.append(row)
    
    # Join all rows with newlines
    return "\n".join(result)