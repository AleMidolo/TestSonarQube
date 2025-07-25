def _fromutc(self, dt):
    """
    Dato un oggetto timezone-aware in un determinato fuso orario, calcola un oggetto datetime con consapevolezza del fuso orario in un nuovo fuso orario.

    Poiché questa è l'unica occasione in cui sappiamo di avere un oggetto datetime non ambiguo, cogliamo questa opportunità per determinare se il datetime è ambiguo e si trova in uno stato di "fold" (ad esempio, se è la prima occorrenza, in ordine cronologico, del datetime ambiguo).

    :param dt:  
        Un oggetto :class:`datetime.datetime` con consapevolezza del fuso orario.
    """
    if dt.tzinfo is not self:
        raise ValueError("fromutc: dt.tzinfo is not self")
    
    # Converti il datetime in UTC
    dt = dt.replace(tzinfo=None)
    timestamp = (dt - datetime(1970, 1, 1)).total_seconds()
    
    # Ottieni il fuso orario locale
    local_dt = datetime.fromtimestamp(timestamp, self)
    
    # Controlla se il datetime è ambiguo
    fold = 0
    if self._fold and local_dt.replace(fold=0) == local_dt.replace(fold=1):
        fold = 1
    
    return local_dt.replace(fold=fold)