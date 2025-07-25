def fromutc(self, dt):
    """Convert aware datetime in UTC to this timezone."""
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)
    
    utc_offset = self.utcoffset(dt)
    if utc_offset is None:
        return dt
    
    # Convert UTC to local time
    dtoff = dt + utc_offset
    
    # Check if we're in a fold
    dst = self.dst(dtoff) 
    if dst is None:
        return dtoff
        
    # If dtoff occurs during DST transition, determine if it's ambiguous
    dtdst = dtoff - dst
    if self.dst(dtdst) != dst:
        # We're in a fold - return first occurrence 
        return dtdst
        
    return dtoff