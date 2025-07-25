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
    fold = 0
    if self.dst(local_dt) is not None:
        # Get timestamps for both possible folds
        fold0_dt = local_dt.replace(fold=0) 
        fold1_dt = local_dt.replace(fold=1)
        
        fold0_ts = (fold0_dt.replace(tzinfo=None) - datetime.datetime(1970,1,1)).total_seconds()
        fold1_ts = (fold1_dt.replace(tzinfo=None) - datetime.datetime(1970,1,1)).total_seconds()
        
        # If original UTC timestamp matches second fold, use fold=1
        if abs(ts - fold1_ts) < abs(ts - fold0_ts):
            fold = 1
            
    return local_dt.replace(fold=fold)