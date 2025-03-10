def _fromutc(self, dt):
    """
    Dato un oggetto timezone-aware in un determinato fuso orario, calcola un oggetto datetime con consapevolezza del fuso orario in un nuovo fuso orario.

    Poiché questa è l'unica occasione in cui sappiamo di avere un oggetto datetime non ambiguo, cogliamo questa opportunità per determinare se il datetime è ambiguo e si trova in uno stato di "fold" (ad esempio, se è la prima occorrenza, in ordine cronologico, del datetime ambiguo).

    :param dt:  
        Un oggetto :class:`datetime.datetime` con consapevolezza del fuso orario.
    """
    if dt.tzinfo is not self:
        raise ValueError("dt deve avere lo stesso fuso orario di self")
    
    # Converti il datetime in UTC
    dt = dt.astimezone(self)
    
    # Controlla se il datetime è ambiguo
    if self._is_ambiguous(dt):
        # Se è ambiguo, imposta fold=1 per indicare la seconda occorrenza
        dt = dt.replace(fold=1)
    
    return dt