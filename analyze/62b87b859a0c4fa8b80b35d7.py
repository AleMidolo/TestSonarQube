def to_csv(self, separator=", ", header=None):
    # Start with header if provided
    result = []
    if header is not None:
        result.append(header + "\n")
    
    # Process each point in the graph
    for point in self.points:
        # Convert coordinates to strings and join with separator
        coords = separator.join(str(coord) for coord in point.coords)
        
        # Convert values to strings and join with separator
        if hasattr(point, 'values') and point.values:
            values = separator.join(str(val) for val in point.values)
            # Combine coordinates and values
            line = coords + separator + values
        else:
            line = coords
            
        # Add newline and append to result
        result.append(line + "\n")
    
    # Join all lines and return
    return "".join(result)