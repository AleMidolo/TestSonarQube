def fromutc(self, dt):
    """
    Dado un objeto "datetime" que contiene información de la zona horaria al que pertenece, calcula un objeto "datetime" para una zona horaria diferente, que contenga información de la nueva zona horaria al que pertenece.

    Dado que esta es la única ocasión en la que *sabemos* que tenemos un objeto datetime no ambiguo, aprovechamos esta oportunidad para determinar si el datetime es ambiguo y está en un estado de "pliegue" (por ejemplo, si es la primera ocurrencia, cronológicamente, del datetime ambiguo).

    :param dt:
        Un objeto :class:`datetime.datetime` con conocimiento de zona horaria.
    """
    # Verificar que el objeto datetime tiene información de zona horaria
    if dt.tzinfo is None:
        raise ValueError("El objeto datetime debe tener información de zona horaria.")

    # Convertir el datetime a la nueva zona horaria
    new_dt = dt.astimezone(self)

    # Determinar si el datetime es ambiguo
    if new_dt.dst() != timedelta(0):
        # Si hay un cambio de horario, verificar si es la primera ocurrencia
        if new_dt < self.utcoffset() + new_dt.dst():
            raise ValueError("El datetime es ambiguo y no se puede determinar su estado.")

    return new_dt