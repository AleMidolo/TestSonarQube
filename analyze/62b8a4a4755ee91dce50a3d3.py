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
        raise ValueError("dt must be timezone-aware")

    # Convert the datetime to UTC
    utc_dt = dt.astimezone(self.utc)

    # Now convert the UTC datetime to the new timezone
    new_tz_dt = utc_dt.astimezone(self)

    # Check for ambiguity
    if new_tz_dt.dst() != timedelta(0):
        # If the new timezone has a daylight saving time transition
        # we need to check if the datetime is in the first or second
        # occurrence of the ambiguous time
        if dt.fold == 0:
            # This is the first occurrence
            return new_tz_dt.replace(fold=0)
        else:
            # This is the second occurrence
            return new_tz_dt.replace(fold=1)
    
    return new_tz_dt