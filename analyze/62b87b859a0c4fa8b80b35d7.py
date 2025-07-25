def to_csv(self, separator=", ", header=None):
    # Start with header if provided
    result = []
    if header is not None:
        result.append(header + "\n")
    
    # Process each point in the graph
    for point in self.points:
        # Convert coordinates to strings
        coord_strs = [str(x) for x in point.coordinates]
        
        # Convert values to strings
        if hasattr(point, 'values'):
            if isinstance(point.values, (list, tuple)):
                value_strs = [str(v) for v in point.values]
            else:
                value_strs = [str(point.values)]
        else:
            value_strs = []
            
        # Combine coordinates and values with separator
        line = separator.join(coord_strs + value_strs)
        result.append(line + "\n")
        
    # Return the complete CSV string
    return "".join(result)