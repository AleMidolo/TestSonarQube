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
    dst_before = self.dst(local_dt - datetime.timedelta(hours=1))
    dst_after = self.dst(local_dt + datetime.timedelta(hours=1)) 
    is_ambiguous = dst_before != dst_after
    
    if is_ambiguous:
        # Set fold=0 for first occurrence of ambiguous datetime
        local_dt = local_dt.replace(fold=0)
        
    return local_dt