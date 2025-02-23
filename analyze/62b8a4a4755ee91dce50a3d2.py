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
    
    # Check if the datetime is ambiguous (in a fold)
    if dt.dst() is not None and dt.dst() != timedelta(0):
        # If there is a daylight saving time transition, check the fold
        if dt.fold == 0:
            # This is the first occurrence of the ambiguous datetime
            new_dt = dt - utc_offset
        else:
            # This is the second occurrence of the ambiguous datetime
            new_dt = dt - utc_offset + dt.dst()
    else:
        # If there is no ambiguity, just convert to UTC
        new_dt = dt - utc_offset

    # Return the new timezone-aware datetime
    return new_dt.replace(tzinfo=self)