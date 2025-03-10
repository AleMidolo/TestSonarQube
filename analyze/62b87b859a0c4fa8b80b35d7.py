def to_csv(self, separator=",", header=None):
    """
    Converts the points of the graph into CSV format.

    Args:
        separator (str): Delimiter for the values, default is a comma.
        header (str, optional): If not None, this string is the first line of the output 
                               (a newline is automatically added).

    Returns:
        str: The CSV representation of the graph.
    """
    csv_lines = []
    
    if header is not None:
        csv_lines.append(header)
    
    for point in self.points:
        # Convert coordinates to string
        coords_str = separator.join(map(str, point.coords))
        # Convert value parts to string
        value_str = separator.join(map(str, point.value))
        # Combine coordinates and value
        csv_line = f"{coords_str}{separator}{value_str}"
        csv_lines.append(csv_line)
    
    return "\n".join(csv_lines)