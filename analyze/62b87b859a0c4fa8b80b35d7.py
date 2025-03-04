def to_csv(self, separator=",", header=None):
    """
    .. deprecated:: 0.5 in Lena 0.5 to_csv non è più utilizzato.  
          Gli iterabili vengono convertiti in tabelle.

    Converte i punti del grafico in formato CSV.

    *separator* delimita i valori, il valore predefinito è la virgola.

    *header*, se non è ``None``, è la prima stringa dell'output  
    (una nuova riga viene aggiunta automaticamente).

    Poiché un grafico può essere multidimensionale,  
    per ogni punto, prima le sue coordinate vengono convertite in stringa  
    (separate da *separator*), poi ogni parte del suo valore.

    Per convertire un :class:`Graph` in formato CSV all'interno di una sequenza Lena,  
    utilizzare :class:`lena.output.ToCSV`.
    """
    import csv
    from io import StringIO

    output = StringIO()
    writer = csv.writer(output, delimiter=separator)

    if header is not None:
        writer.writerow([header])

    for point in self.points:  # Assuming self.points is an iterable of points
        row = [str(coord) for coord in point.coordinates]  # Convert coordinates to strings
        row.extend([str(value) for value in point.values])  # Convert values to strings
        writer.writerow(row)

    return output.getvalue()