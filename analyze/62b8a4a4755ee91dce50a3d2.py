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
        raise ValueError("The input datetime must be timezone-aware.")

    # Convert the datetime to UTC
    utc_dt = dt.astimezone(self.utc)

    # Convert the UTC datetime to the target timezone
    local_dt = utc_dt.astimezone(self)

    # Check if the datetime is ambiguous in the target timezone
    if self._is_ambiguous(local_dt):
        # If the original datetime was in a fold, keep it in the fold
        if dt.fold:
            local_dt = local_dt.replace(fold=1)
        else:
            local_dt = local_dt.replace(fold=0)

    return local_dt