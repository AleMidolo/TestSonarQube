def to_csv(self, separator=",", header=None):
    """
    Convert the points of the graph to CSV format.

    Args:
        separator (str): The character used to separate values, default is comma.
        header (str, optional): If not None, this will be the first string in the output
                                (a newline is automatically added).

    Returns:
        str: A string representing the graph points in CSV format.
    """
    csv_lines = []
    
    # Add header if provided
    if header is not None:
        csv_lines.append(header)
    
    # Iterate over each point in the graph
    for point in self.points:
        # Convert coordinates to string separated by the separator
        coords_str = separator.join(map(str, point.coordinates))
        # Convert values to string separated by the separator
        values_str = separator.join(map(str, point.values))
        # Combine coordinates and values into a single line
        csv_line = f"{coords_str}{separator}{values_str}"
        csv_lines.append(csv_line)
    
    # Join all lines with newline characters
    return "\n".join(csv_lines)