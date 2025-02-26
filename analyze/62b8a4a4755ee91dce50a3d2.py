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

    # Convert the datetime to UTC
    utc_dt = dt.astimezone(self.utc)

    # Check if the datetime is ambiguous
    if self.is_ambiguous(utc_dt):
        # Determine if it's in the first or second fold
        if self.fold == 0:
            return utc_dt.replace(fold=0)
        else:
            return utc_dt.replace(fold=1)
    
    return utc_dt