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
    # Ensure input is timezone-aware and in UTC
    if dt.tzinfo is not self:
        dt = dt.astimezone(self)

    # Calculate UTC offset for the given datetime
    utc_offset = self.utcoffset(dt)
    if utc_offset is None:
        return dt

    # Add the offset to get local time
    local_dt = dt + utc_offset

    # Check if datetime is ambiguous (in DST transition)
    dst_offset = self.dst(local_dt)
    if dst_offset is None:
        return local_dt

    # Calculate fold status
    # If we're in a fold, the actual offset should be different than the one we used
    actual_offset = self.utcoffset(local_dt)
    if actual_offset != utc_offset:
        # We're in a fold, adjust the datetime
        local_dt = dt + actual_offset
        local_dt = local_dt.replace(fold=1)
    else:
        local_dt = local_dt.replace(fold=0)

    return local_dt