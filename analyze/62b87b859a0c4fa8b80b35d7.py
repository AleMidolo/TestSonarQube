def to_csv(self, separator=",", header=None):
    """
    Converts the points of the graph into CSV format.

    Args:
        separator (str): Delimiter for values, default is a comma.
        header (str, optional): If not None, this string is the first line of the output 
                               (a newline is automatically added).

    Returns:
        str: The CSV representation of the graph.
    """
    csv_lines = []
    
    # Add header if provided
    if header is not None:
        csv_lines.append(header)
    
    # Convert each point to CSV format
    for point in self.points:
        # Convert coordinates to string
        coords_str = separator.join(map(str, point.coordinates))
        # Convert value parts to string
        value_str = separator.join(map(str, point.value))
        # Combine coordinates and value
        csv_line = f"{coords_str}{separator}{value_str}"
        csv_lines.append(csv_line)
    
    # Join all lines with newline characters
    return "\n".join(csv_lines)