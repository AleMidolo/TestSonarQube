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
    
    # Verifica se il datetime è ambiguo (cade in un periodo di transizione DST)
    dst_offset = self.dst(dt)
    if dst_offset is None:
        return dt
        
    # Se c'è un offset DST, determina se siamo nel "fold"
    # Confronta con il datetime un'ora prima
    earlier = dt - dst_offset
    if self.dst(earlier) is not None:
        # Se il datetime precedente ha un offset DST diverso,
        # siamo nel periodo di transizione
        fold = self.dst(earlier) != dst_offset
        return dt.replace(fold=fold)
        
    return dt