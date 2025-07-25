def _fromutc(self, dt):
    """
    Dado un objeto 'datetime' consciente de la zona horaria en una zona horaria específica, calcula un objeto 'datetime' consciente de la zona horaria en una nueva zona horaria.

    Dado que esta es la única ocasión en la que *sabemos* que tenemos un objeto 'datetime' no ambiguo, aprovechamos esta oportunidad para determinar si el 'datetime' es ambiguo y está en un estado de "pliegue" (por ejemplo, si es la primera ocurrencia, cronológicamente, del 'datetime' ambiguo).

    :param dt:  
        Un objeto :class:`datetime.datetime` consciente de la zona horaria.
    """
    if dt.tzinfo is not self:
        raise ValueError("El objeto datetime no está en la zona horaria correcta.")
    
    # Convertir el datetime a UTC
    utc_dt = dt.astimezone(self.utc)
    
    # Convertir el datetime UTC a la nueva zona horaria
    new_dt = utc_dt.astimezone(self)
    
    # Verificar si el datetime es ambiguo en la nueva zona horaria
    if self.is_ambiguous(new_dt):
        # Si es ambiguo, ajustar al primer pliegue
        new_dt = self._fold_first(new_dt)
    
    return new_dt