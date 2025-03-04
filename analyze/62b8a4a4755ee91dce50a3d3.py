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
    if dst_offset is None:
        return dt
        
    # Se c'è una transizione DST, determina se siamo nel fold
    standard_offset = self.utcoffset(dt) - dst_offset
    transition_fold = (standard_offset.total_seconds() > 0)
    
    # Imposta il fold appropriato
    return dt.replace(fold=transition_fold)