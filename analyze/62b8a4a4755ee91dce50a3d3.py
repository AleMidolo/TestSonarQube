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
    local_dt = dt.fromtimestamp(utc_ts + local_offset.total_seconds())
    
    # Verificar si el datetime es ambiguo (está en un "pliegue")
    fold = 0
    transition_times = self._get_transition_times()
    if transition_times:
        # Buscar la transición más cercana
        for trans_time, is_dst in transition_times:
            if abs(trans_time - utc_ts) < 3600:  # dentro de 1 hora
                prev_offset = self.utcoffset(dt - timedelta(hours=1))
                next_offset = self.utcoffset(dt + timedelta(hours=1))
                
                if prev_offset != next_offset:
                    # Estamos en una transición
                    fold = 1 if local_offset == min(prev_offset, next_offset) else 0
                break
    
    return local_dt.replace(tzinfo=self, fold=fold)