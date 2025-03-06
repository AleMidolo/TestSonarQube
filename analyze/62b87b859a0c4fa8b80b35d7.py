def to_csv(self, separator=",", header=None):
    """
    .. deprecated:: 0.5 in Lena 0.5 to_csv is not used.
          Iterables are converted to tables.

    Convert graph's points to CSV.

    *separator* delimits values, the default is comma.

    *header*, if not ``None``, is the first string of the output
    (new line is added automatically).

    Since a graph can be multidimensional,
    for each point first its coordinate is converted to string
    (separated by *separator*), then each part of its value.

    To convert :class:`Graph` to CSV inside a Lena sequence,
    use :class:`lena.output.ToCSV`.
    """
    csv_lines = []
    
    if header is not None:
        csv_lines.append(header)
    
    for point in self.points:
        # Convert coordinate to string
        coord_str = separator.join(map(str, point.coordinate))
        # Convert value to string
        value_str = separator.join(map(str, point.value))
        # Combine coordinate and value
        csv_line = f"{coord_str}{separator}{value_str}"
        csv_lines.append(csv_line)
    
    return "\n".join(csv_lines)