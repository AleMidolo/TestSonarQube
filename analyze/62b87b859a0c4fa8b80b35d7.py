def to_csv(self, separator=",", header=None):
    """
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
    csv_lines = []
    
    if header is not None:
        csv_lines.append(header)
    
    for point in self.points:
        # Convert coordinates to string separated by the separator
        coords_str = separator.join(map(str, point.coords))
        # Convert values to string separated by the separator
        values_str = separator.join(map(str, point.values))
        # Combine coordinates and values
        csv_line = f"{coords_str}{separator}{values_str}"
        csv_lines.append(csv_line)
    
    return "\n".join(csv_lines)