def fromutc(self, dt):
    """Convert aware datetime in UTC to this timezone."""
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)
    
    utc_offset = self.utcoffset(dt)
    if utc_offset is None:
        return dt
    
    # Convert to UTC
    dt = dt + utc_offset
    
    # Check if datetime falls in DST transition
    dst = self.dst(dt)
    if dst is None:
        return dt
        
    # Adjust for DST if needed
    return dt + dst