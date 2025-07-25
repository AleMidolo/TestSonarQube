def fromutc(self, dt):
    """
    Dado un objeto "datetime" que contiene información de la zona horaria al que pertenece, calcula un objeto "datetime" para una zona horaria diferente, que contenga información de la nueva zona horaria al que pertenece.

    Dado que esta es la única ocasión en la que *sabemos* que tenemos un objeto datetime no ambiguo, aprovechamos esta oportunidad para determinar si el datetime es ambiguo y está en un estado de "pliegue" (por ejemplo, si es la primera ocurrencia, cronológicamente, del datetime ambiguo).

    :param dt:
        Un objeto :class:`datetime.datetime` con conocimiento de zona horaria.
    """
    if dt.tzinfo is not self:
        dt = dt.astimezone(self)

    utc_offset = dt.utcoffset()
    if utc_offset is None:
        return dt

    # Convertir a timestamp UTC
    utc_ts = (dt - utc_offset).timestamp()
    
    # Obtener el offset local para este timestamp
    local_offset = self.utcoffset(dt)
    
    # Calcular el nuevo datetime
    local_dt = dt + (local_offset - utc_offset)
    
    # Verificar si estamos en un periodo ambiguo (pliegue)
    fold = 0
    if self._fold_status(local_dt):
        # Si hay ambigüedad, verificamos si es la primera ocurrencia
        prev_offset = self.utcoffset(local_dt.replace(fold=0))
        next_offset = self.utcoffset(local_dt.replace(fold=1))
        
        if prev_offset > next_offset:
            # Estamos en un periodo de transición DST->STD
            fold = utc_ts >= (local_dt.replace(fold=0) - prev_offset).timestamp()
            
    return local_dt.replace(tzinfo=self, fold=fold)

def _fold_status(self, dt):
    """Helper method para detectar si un datetime está en un periodo ambiguo"""
    try:
        prev_offset = self.utcoffset(dt.replace(fold=0))
        next_offset = self.utcoffset(dt.replace(fold=1))
        return prev_offset != next_offset
    except:
        return False