from datetime import datetime, timedelta

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
    
    # Calcular el offset para la nueva zona horaria
    offset = self.utcoffset(dt_utc)
    
    # Aplicar el offset al datetime UTC
    dt_new = dt_utc + offset
    
    # Asegurarse de que el nuevo datetime tenga la zona horaria correcta
    dt_new = dt_new.replace(tzinfo=self)
    
    return dt_new