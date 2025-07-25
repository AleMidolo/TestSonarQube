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
    # Assuming self.points is a list of tuples representing the graph points
    output = []
    
    if header is not None:
        output.append(header)
    
    for point in self.points:
        # Convert each point to a string with the specified separator
        point_str = separator.join(map(str, point))
        output.append(point_str)
    
    return "\n".join(output)