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
    
    # Agregar el encabezado si está presente
    if header is not None:
        csv_lines.append(header)
    
    # Convertir cada punto a formato CSV
    for point in self.points:
        # Convertir la coordenada a cadena
        coord_str = separator.join(map(str, point.coordinate))
        # Convertir el valor a cadena
        value_str = separator.join(map(str, point.value))
        # Combinar coordenada y valor
        csv_line = f"{coord_str}{separator}{value_str}"
        csv_lines.append(csv_line)
    
    # Unir todas las líneas con saltos de línea
    return "\n".join(csv_lines)