def to_csv(self, separator=",", header=None):
    import csv
    from io import StringIO

    output = StringIO()
    writer = csv.writer(output, delimiter=separator)

    if header is not None:
        writer.writerow([header])

    for point in self.points:
        row = [str(coord) for coord in point.coordinates]
        for value in point.values:
            row.append(str(value))
        writer.writerow(row)

    return output.getvalue()