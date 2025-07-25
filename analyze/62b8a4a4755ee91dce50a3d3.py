def fromutc(self, dt):
    # Verifica che dt sia un datetime con timezone
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)
    
    # Ottieni l'offset UTC per questo datetime
    utc_offset = self.utcoffset(dt)
    
    if utc_offset is None:
        return dt
    
    # Calcola il nuovo datetime aggiungendo l'offset UTC
    dt = dt + utc_offset
    
    # Gestione del fold per datetime ambigui
    dst_offset = self.dst(dt)
    if dst_offset is not None:
        # Se c'è un cambio DST, verifica se il datetime è ambiguo
        standard_offset = self.utcoffset(dt - dst_offset)
        if standard_offset is not None:
            # Se gli offset sono diversi, il datetime è ambiguo
            if standard_offset != utc_offset:
                # Imposta fold=1 se questo è il primo datetime nell'ambiguità
                fold = 1 if standard_offset > utc_offset else 0
                dt = dt.replace(fold=fold)
    
    return dt