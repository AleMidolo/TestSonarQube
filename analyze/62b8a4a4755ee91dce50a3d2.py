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
    if dt.fold == 1:
        # If it's in the second occurrence of the ambiguous time, adjust accordingly
        dt = dt - utc_offset

    # Convert to the new timezone
    new_dt = dt.astimezone(self)

    return new_dt