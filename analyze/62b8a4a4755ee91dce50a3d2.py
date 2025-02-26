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
        raise ValueError("dt must be a timezone-aware datetime")

    # Get the UTC offset for the given datetime
    utc_offset = dt.utcoffset()
    
    # Convert the datetime to UTC
    utc_dt = dt - utc_offset
    
    # Now convert the UTC datetime to the new timezone
    new_dt = utc_dt.astimezone(self)

    # Check for ambiguity in the new timezone
    if new_dt.dst() != timedelta(0):
        # If the new datetime has a non-zero DST offset, it may be ambiguous
        if new_dt.fold == 0:
            # If it's the first occurrence, we return it as is
            return new_dt
        else:
            # If it's the second occurrence, we need to adjust
            return new_dt - new_dt.dst()
    
    return new_dt