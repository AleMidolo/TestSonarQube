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
    
    # Create local datetime
    local_dt = datetime.datetime.fromtimestamp(ts, self)
    
    # Check if datetime is ambiguous (in DST transition)
    dst_before = self.dst(local_dt - datetime.timedelta(hours=1))
    dst_after = self.dst(local_dt + datetime.timedelta(hours=1))
    
    if dst_before != dst_after:
        # We're in a DST transition
        fold = 0
        if dst_before > dst_after:
            # Transitioning out of DST
            fold = 1
        local_dt = local_dt.replace(fold=fold)
        
    return local_dt