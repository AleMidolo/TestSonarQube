def _fromutc(self, dt):
    """
    Dado un objeto 'datetime' consciente de la zona horaria en una zona horaria específica, calcula un objeto 'datetime' consciente de la zona horaria en una nueva zona horaria.

    Dado que esta es la única ocasión en la que *sabemos* que tenemos un objeto 'datetime' no ambiguo, aprovechamos esta oportunidad para determinar si el 'datetime' es ambiguo y está en un estado de "pliegue" (por ejemplo, si es la primera ocurrencia, cronológicamente, del 'datetime' ambiguo).

    :param dt:  
        Un objeto :class:`datetime.datetime` consciente de la zona horaria.
    """
    # Verificar que el objeto dt es consciente de la zona horaria
    if dt.tzinfo is None:
        raise ValueError("El objeto datetime debe ser consciente de la zona horaria")

    # Convertir el datetime a la nueva zona horaria
    new_dt = dt.astimezone(self)

    # Determinar si el datetime es ambiguo
    if new_dt.dst() != timedelta(0):
        # Si hay un cambio de horario, verificar si es la primera ocurrencia
        if new_dt < self.utcoffset() + new_dt.dst():
            return new_dt - new_dt.dst()
    
    return new_dt