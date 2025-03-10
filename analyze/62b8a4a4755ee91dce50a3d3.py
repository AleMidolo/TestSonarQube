def fromutc(self, dt):
    """
    Dado un objeto "datetime" que contiene información de la zona horaria al que pertenece, calcula un objeto "datetime" para una zona horaria diferente, que contenga información de la nueva zona horaria al que pertenece.

    Dado que esta es la única ocasión en la que *sabemos* que tenemos un objeto datetime no ambiguo, aprovechamos esta oportunidad para determinar si el datetime es ambiguo y está en un estado de "pliegue" (por ejemplo, si es la primera ocurrencia, cronológicamente, del datetime ambiguo).

    :param dt:
        Un objeto :class:`datetime.datetime` con conocimiento de zona horaria.
    """
    if dt.tzinfo is None:
        raise ValueError("fromutc() requires a timezone-aware datetime")
    
    # Convertir el datetime a UTC
    dt_utc = dt.astimezone(self)
    
    # Verificar si el datetime es ambiguo
    if self._is_ambiguous(dt_utc):
        # Si es ambiguo, determinar si está en el "pliegue"
        if self._fold(dt_utc):
            # Si está en el pliegue, ajustar el datetime
            dt_utc = dt_utc.replace(fold=1)
    
    return dt_utc