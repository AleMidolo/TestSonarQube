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
    import warnings
    warnings.warn(
        "to_csv is deprecated since Lena 0.5. Use lena.output.ToCSV instead.",
        DeprecationWarning,
        stacklevel=2
    )
    
    csv_lines = []
    
    if header is not None:
        csv_lines.append(header)
    
    for point in self.points:
        # Convert coordinates to string separated by the separator
        coord_str = separator.join(map(str, point.coordinates))
        # Convert values to string separated by the separator
        value_str = separator.join(map(str, point.values))
        # Combine coordinates and values
        csv_line = f"{coord_str}{separator}{value_str}"
        csv_lines.append(csv_line)
    
    return "\n".join(csv_lines)