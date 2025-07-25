def fromutc(self, dt):
    # Verifica che dt sia timezone-aware e in UTC
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)
    
    # Ottieni l'offset UTC per questo datetime
    utc_offset = self.utcoffset(dt)
    if utc_offset is None:
        return dt
    
    # Calcola il nuovo datetime aggiungendo l'offset UTC
    dt = dt + utc_offset
    
    # Gestisci il caso di datetime ambigui
    dst_offset = self.dst(dt)
    if dst_offset is None:
        return dt
    
    # Se c'è un cambio DST, determina se siamo nel "fold"
    # confrontando gli offset
    fold = False
    if dst_offset != self.dst(dt - utc_offset):
        # Se l'offset DST è cambiato, siamo nel fold se
        # il nuovo offset è minore del precedente
        fold = dst_offset < self.dst(dt - utc_offset)
        
    return dt.replace(fold=fold)