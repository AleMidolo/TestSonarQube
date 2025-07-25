def fromutc(self, dt):
    """Convert aware datetime in UTC to this timezone."""
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)
    
    utc_offset = self.utcoffset(dt)
    if utc_offset is None:
        return dt
    
    # Convert UTC to local time
    dtoff = dt.replace(tzinfo=None) + utc_offset
    
    # Check if we're in a fold
    dst_offset = self.dst(dtoff)
    if dst_offset is None:
        return dtoff.replace(tzinfo=self)
        
    # If standard offset and DST offset are the same, no fold
    std_offset = self.utcoffset(dtoff) - dst_offset
    if std_offset == utc_offset:
        return dtoff.replace(tzinfo=self)
        
    # We're in a fold - check if this is the first occurrence
    dtdst = dtoff - dst_offset
    if self.dst(dtdst) is None:
        return dtdst.replace(tzinfo=self)
        
    return dtoff.replace(tzinfo=self)