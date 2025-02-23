def _fromutc(self, dt):
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
        raise ValueError("dt must be timezone-aware")

    # Get the UTC offset for the given datetime
    utc_offset = dt.utcoffset()
    
    # Convert the datetime to UTC
    utc_dt = dt - utc_offset
    
    # Now convert the UTC datetime to the new timezone
    new_dt = utc_dt.astimezone(self)

    # Check for ambiguity in the new timezone
    if new_dt.dst() != timedelta(0) and new_dt.fold == 0:
        # If the datetime is ambiguous, we need to determine the correct fold
        # Here we assume that the first occurrence is the one we want
        new_dt = new_dt.replace(fold=1)

    return new_dt