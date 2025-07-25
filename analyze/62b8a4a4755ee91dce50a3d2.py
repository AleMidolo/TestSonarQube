def _fromutc(self, dt):
    """Convert aware datetime in UTC to this timezone."""
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)
    
    utc_offset = self.utcoffset(dt)
    if utc_offset is None:
        return dt
    
    # Convert to timestamp, add offset and create new datetime
    ts = (dt.replace(tzinfo=None) - datetime.datetime(1970,1,1)).total_seconds()
    ts += utc_offset.total_seconds()
    
    # Create local datetime from timestamp
    local_dt = datetime.datetime.fromtimestamp(ts, self)
    
    # Check if datetime is ambiguous (in DST transition)
    dst_offset = self.dst(local_dt)
    if dst_offset is not None:
        # Get standard offset
        std_offset = utc_offset - dst_offset
        # Check if datetime occurs twice
        ts_std = ts - dst_offset.total_seconds()
        local_std = datetime.datetime.fromtimestamp(ts_std, self)
        
        # If both standard and DST times exist, set fold accordingly
        if local_std.replace(fold=0) == local_dt.replace(fold=0):
            return local_dt.replace(fold=1 if ts_std > ts else 0)
            
    return local_dt