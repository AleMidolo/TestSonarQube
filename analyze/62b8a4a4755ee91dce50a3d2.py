def _fromutc(self, dt):
    """
    Dado un objeto 'datetime' consciente de la zona horaria en una zona horaria específica, calcula un objeto 'datetime' consciente de la zona horaria en una nueva zona horaria.

    Dado que esta es la única ocasión en la que *sabemos* que tenemos un objeto 'datetime' no ambiguo, aprovechamos esta oportunidad para determinar si el 'datetime' es ambiguo y está en un estado de "pliegue" (por ejemplo, si es la primera ocurrencia, cronológicamente, del 'datetime' ambiguo).

    :param dt:  
        Un objeto :class:`datetime.datetime` consciente de la zona horaria.
    """
    if dt.tzinfo is None:
        raise ValueError("El objeto datetime debe ser consciente de la zona horaria.")
    
    # Convertir el datetime a UTC
    dt_utc = dt.astimezone(self.utc)
    
    # Convertir el datetime UTC a la nueva zona horaria
    dt_local = dt_utc.astimezone(self)
    
    # Verificar si el datetime es ambiguo en la nueva zona horaria
    if self.is_ambiguous(dt_local):
        # Si es ambiguo, ajustar para la primera ocurrencia
        dt_local = self.resolve_ambiguity(dt_local, first=True)
    
    return dt_local