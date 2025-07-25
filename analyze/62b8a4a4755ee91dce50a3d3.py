from datetime import datetime, timedelta

def fromutc(self, dt):
    """
    Dato un oggetto datetime con consapevolezza del fuso orario (timezone-aware) in un determinato fuso orario, calcola un oggetto datetime con consapevolezza del fuso orario in un nuovo fuso orario.

    Poiché questa è l'unica occasione in cui *sappiamo* di avere un oggetto datetime non ambiguo, cogliamo l'opportunità per determinare se il datetime è ambiguo e si trova in uno stato di "fold" (ad esempio, se è la prima occorrenza, in ordine cronologico, del datetime ambiguo).

    :param dt:  
        Un oggetto :class:`datetime.datetime` con consapevolezza del fuso orario (timezone-aware).
    """
    if dt.tzinfo is None:
        raise ValueError("fromutc() requires a timezone-aware datetime object")
    
    # Convert the datetime to UTC
    dt_utc = dt.astimezone(self.utc)
    
    # Calculate the offset from UTC for the new timezone
    offset = self.utcoffset(dt_utc)
    
    # Apply the offset to get the new datetime
    new_dt = dt_utc + offset
    
    # Check if the new datetime is ambiguous (e.g., during a DST transition)
    if self.is_ambiguous(new_dt):
        # If ambiguous, set the fold attribute to 1 (second occurrence)
        new_dt = new_dt.replace(fold=1)
    
    return new_dt