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
        standard_offset = self.utcoffset(dt - dst_offset) - dst_offset
        transition_fold = ((utc_offset - dst_offset) != standard_offset)
        
        if transition_fold:
            # Il datetime è ambiguo, imposta fold=1 per la seconda occorrenza
            return dt.replace(fold=1)
            
    return dt