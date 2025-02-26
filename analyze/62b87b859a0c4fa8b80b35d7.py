def to_csv(self, separator=",", header=None):
    """
    .. deprecated:: 0.5 en Lena 0.5 to_csv ya no se utiliza.
          Los iterables se convierten en tablas.

    Convierte los puntos del gráfico a formato CSV.

    *separator* delimita los valores, el valor predeterminado es una coma.

    *header*, si no es ``None``, es la primera línea de la salida
    (se agrega automáticamente un salto de línea).

    Dado que un gráfico puede ser multidimensional,
    para cada punto, primero su coordenada se convierte en una cadena
    (separada por *separator*), y luego cada parte de su valor.

    Para convertir un :class:`Graph` a formato CSV dentro de una secuencia de Lena,
    utiliza :class:`lena.output.ToCSV`.
    """
    import csv
    from io import StringIO

    output = StringIO()
    writer = csv.writer(output, delimiter=separator)

    if header is not None:
        writer.writerow(header)

    for point in self.points:  # Assuming self.points is a list of points
        row = [str(coord) for coord in point]  # Convert coordinates to strings
        writer.writerow(row)

    return output.getvalue()