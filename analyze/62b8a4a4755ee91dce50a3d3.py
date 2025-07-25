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

    # Convert the datetime to UTC
    dt_utc = dt.astimezone(self.utc)

    # Convert the UTC datetime to the new timezone
    dt_new = dt_utc.astimezone(self)

    # Check if the datetime is ambiguous in the new timezone
    if dt_new.fold:
        # If it's ambiguous, adjust the datetime to the first occurrence
        dt_new = dt_new.replace(fold=0)

    return dt_new