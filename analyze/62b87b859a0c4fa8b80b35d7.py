def to_csv(self, separator=",", header=None):
    """
    Converts the points of the graph into CSV format.

    Args:
        separator (str): Delimiter for values, default is a comma.
        header (str, optional): If not None, it is the first string of the output 
                               (a new line is automatically added).

    Returns:
        str: The CSV formatted string representing the graph points.
    """
    csv_lines = []
    
    if header is not None:
        csv_lines.append(header)
    
    for point in self.points:
        # Convert coordinates to string separated by the separator
        coords_str = separator.join(map(str, point.coordinates))
        # Convert each part of the value to string
        value_str = separator.join(map(str, point.value))
        # Combine coordinates and value into a single line
        csv_line = f"{coords_str}{separator}{value_str}"
        csv_lines.append(csv_line)
    
    return "\n".join(csv_lines)