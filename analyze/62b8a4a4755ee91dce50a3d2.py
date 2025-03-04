def _fromutc(self, dt):
    """
    Dado un objeto 'datetime' consciente de la zona horaria en una zona horaria específica, calcula un objeto 'datetime' consciente de la zona horaria en una nueva zona horaria.

    Dado que esta es la única ocasión en la que *sabemos* que tenemos un objeto 'datetime' no ambiguo, aprovechamos esta oportunidad para determinar si el 'datetime' es ambiguo y está en un estado de "pliegue" (por ejemplo, si es la primera ocurrencia, cronológicamente, del 'datetime' ambiguo).

    :param dt:  
        Un objeto :class:`datetime.datetime` consciente de la zona horaria.
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
    
    # Calcular el datetime local
    local_dt = dt + (local_offset - utc_offset)
    
    # Verificar si el datetime es ambiguo (está en un "pliegue")
    timestamps = []
    
    # Probar offsets antes y después
    for offset in [local_offset - timedelta(hours=1), local_offset, local_offset + timedelta(hours=1)]:
        try:
            local_ts = (dt.replace(tzinfo=None) - offset).timestamp()
            timestamps.append(local_ts)
        except:
            continue
            
    # Si hay múltiples timestamps posibles, estamos en un pliegue
    is_fold = len(set(timestamps)) > 1
    
    if is_fold:
        # Marcar como primera ocurrencia si es el timestamp más temprano
        local_dt = local_dt.replace(fold=utc_ts == min(timestamps))
        
    return local_dt