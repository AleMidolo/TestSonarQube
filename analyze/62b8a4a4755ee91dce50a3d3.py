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
    dt_utc = dt.astimezone(self.utc)
    
    # Convertir el datetime UTC a la nueva zona horaria
    dt_local = dt_utc.astimezone(self)
    
    # Verificar si el datetime es ambiguo en la nueva zona horaria
    if self.is_ambiguous(dt_local):
        # Si es ambiguo, ajustar para que sea la primera ocurrencia
        dt_local = self.resolve_ambiguity(dt_local, first=True)
    
    return dt_local