def _fromutc(self, dt):
    # Ensure dt is timezone-aware and in UTC
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)
    
    # Get UTC offset for the datetime
    utc_offset = self.utcoffset(dt)
    if utc_offset is None:
        return dt
    
    # Add the offset to get local time
    local_dt = dt + utc_offset
    
    # Check if this time is ambiguous (falls in DST transition)
    dst_offset = self.dst(local_dt)
    if dst_offset is None:
        return local_dt
        
    # If we're in DST transition period
    standard_offset = self.utcoffset(local_dt - dst_offset)
    if standard_offset is None:
        return local_dt
        
    # Check if datetime is ambiguous
    if standard_offset != utc_offset:
        # Get both possible times
        earlier = local_dt - dst_offset
        later = local_dt
        
        # Return earlier time by default for ambiguous times
        if earlier.replace(tzinfo=None) <= dt.replace(tzinfo=None):
            return earlier
        return later
        
    return local_dt