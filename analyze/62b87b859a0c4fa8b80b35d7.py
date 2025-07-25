def to_csv(self, separator=", ", header=None):
    """
    .. deprecated:: 0.5
        In Lena 0.5, `to_csv` is no longer used.
        Iterables will be converted to tables.

    Convert the points of the graph to CSV format.

    *separator* is used to separate values, default is a comma.

    *header* if not ``None``, will be the first line of the output
    (a newline will be automatically added).

    Since the graph can be multidimensional,
    for each point, first convert its coordinates to a string
    (separated by *separator*), and then process each part of its value.

    To convert :class:`Graph` to CSV in a Lena sequence,
    use :class:`lena.output.ToCSV`.
    """
    if header is not None:
        output = [header + "\n"]
    else:
        output = []

    for point in self.points:
        # Convert coordinates to string
        coords = separator.join(map(str, point.coordinates))
        # Convert values to string
        values = separator.join(map(str, point.values))
        output.append(f"{coords}{separator}{values}\n")

    return "".join(output)