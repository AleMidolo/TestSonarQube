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
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)

    utc_offset = self._transition_info(dt.replace(fold=0))[0]
    dt_out = dt + utc_offset

    # Check if we're in a fold
    if self._fold_status(dt_out):
        return dt_out.replace(fold=1)
    else:
        return dt_out.replace(fold=0)