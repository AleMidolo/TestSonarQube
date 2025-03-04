def _fromutc(self, dt):
    """Convert aware datetime in UTC to this timezone."""
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)
    
    utc_offset = self.utcoffset(dt)
    if utc_offset is None:
        return dt
    
    # Convert to timestamp, add offset and convert back
    ts = (dt.replace(tzinfo=None) - datetime.datetime(1970,1,1)).total_seconds()
    ts += utc_offset.total_seconds()
    
    # Create new datetime in local time
    local_dt = datetime.datetime.fromtimestamp(ts, self)
    
    # Check if datetime is ambiguous (in DST transition)
    dst_offset = self.dst(local_dt)
    if dst_offset is not None:
        # Get standard offset
        std_offset = utc_offset - dst_offset
        # Check if we're in fold
        ts_std = ts - dst_offset.total_seconds()
        local_dt_std = datetime.datetime.fromtimestamp(ts_std, self)
        
        if local_dt == local_dt_std:
            # Datetime is ambiguous, set fold=1 for second occurrence
            return local_dt.replace(fold=1)
    
    return local_dt