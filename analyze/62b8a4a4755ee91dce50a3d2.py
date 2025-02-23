def _fromutc(self, dt):
    """
    Dato un oggetto timezone-aware  in un determinato fuso orario, calcola un oggetto datetime con consapevolezza del fuso orario in un nuovo fuso orario.

    Poiché questa è l'unica occasione in cui sappiamo di avere un oggetto datetime non ambiguo, cogliamo questa opportunità per determinare se il datetime è ambiguo e si trova in uno stato di "fold" (ad esempio, se è la prima occorrenza, in ordine cronologico, del datetime ambiguo).

    :param dt:  
        Un oggetto :class:`datetime.datetime` con consapevolezza del fuso orario.
    """
    # Verifica se l'oggetto datetime è consapevole del fuso orario
    if dt.tzinfo is None:
        raise ValueError("L'oggetto datetime deve essere timezone-aware.")

    # Calcola il nuovo datetime in base al fuso orario attuale
    new_dt = dt.astimezone(self)

    # Controlla se il datetime è ambiguo
    if new_dt.fold == 1:
        # Se è in stato di "fold", restituisci la prima occorrenza
        return new_dt.replace(fold=0)
    
    return new_dt