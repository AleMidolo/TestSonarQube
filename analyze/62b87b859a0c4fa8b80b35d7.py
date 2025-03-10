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
    
    if header is not None:
        csv_lines.append(header)
    
    for point in self.points:
        # Convert coordinates to string
        coords = separator.join(map(str, point.coords))
        # Convert value parts to string
        value_parts = separator.join(map(str, point.value))
        # Combine coordinates and value parts
        csv_line = f"{coords}{separator}{value_parts}"
        csv_lines.append(csv_line)
    
    return "\n".join(csv_lines)