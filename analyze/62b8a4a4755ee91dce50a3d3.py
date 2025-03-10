def fromutc(self, dt):
    """
    Given a timezone-aware datetime in a given timezone, calculates a
    timezone-aware datetime in a new timezone.

    Since this is the one time that we *know* we have an unambiguous
    datetime object, we take this opportunity to determine whether the
    datetime is ambiguous and in a "fold" state (e.g. if it's the first
    occurrence, chronologically, of the ambiguous datetime).

    :param dt:
        A timezone-aware :class:`datetime.datetime` object.
    """
    if dt.tzinfo is None:
        raise ValueError("fromutc() requires a timezone-aware datetime")
    
    # Convert the datetime to the new timezone
    new_dt = dt.astimezone(self)
    
    # Check if the datetime is ambiguous in the new timezone
    if self.is_ambiguous(new_dt):
        # If the original datetime was in a fold state, keep it in the fold
        if dt.fold:
            new_dt = new_dt.replace(fold=1)
        else:
            new_dt = new_dt.replace(fold=0)
    
    return new_dt