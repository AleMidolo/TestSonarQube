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
    result = []
    
    # Add header if provided
    if header is not None:
        result.append(str(header))
    
    # Convert each point to CSV format
    for point in self:
        # Convert coordinates to string
        if isinstance(point[0], (list, tuple)):
            coord_str = separator.join(str(x) for x in point[0])
        else:
            coord_str = str(point[0])
            
        # Convert values to string
        if isinstance(point[1], (list, tuple)):
            value_str = separator.join(str(x) for x in point[1])
        else:
            value_str = str(point[1])
            
        # Combine coordinates and values
        row = coord_str + separator + value_str
        result.append(row)
    
    # Join all rows with newlines
    return "\n".join(result)