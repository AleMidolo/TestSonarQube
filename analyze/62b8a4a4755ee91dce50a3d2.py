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
    fold = 0
    if self.dst(local_dt) is not None:
        # Get timestamps for both possible folds
        local_dt0 = local_dt.replace(fold=0) 
        local_dt1 = local_dt.replace(fold=1)
        
        ts0 = (local_dt0.replace(tzinfo=None) - datetime.datetime(1970,1,1)).total_seconds()
        ts1 = (local_dt1.replace(tzinfo=None) - datetime.datetime(1970,1,1)).total_seconds()
        
        # If original timestamp is closer to second fold, use fold=1
        if abs(ts - ts1) < abs(ts - ts0):
            fold = 1
            
    return local_dt.replace(fold=fold)