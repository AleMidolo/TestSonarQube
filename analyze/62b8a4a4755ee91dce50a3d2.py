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
    # Check if input datetime is timezone aware and in UTC
    if dt.tzinfo is not self:
        dt = dt.replace(tzinfo=self)

    utc_offset = self.utcoffset(dt)
    if utc_offset is None:
        return dt

    # Convert to local time by adding UTC offset
    dt = dt + utc_offset

    # Check if datetime is ambiguous (in DST transition)
    dst_offset = self.dst(dt)
    if dst_offset is None:
        return dt

    # Calculate fold by checking if we're in a DST transition
    fold = 0
    if self.is_ambiguous(dt):
        # Get the previous UTC offset
        prev_dt = dt - dst_offset
        prev_offset = self.utcoffset(prev_dt)
        
        if prev_offset is not None:
            # If current offset is less than previous, we're in fold=1
            fold = 1 if utc_offset < prev_offset else 0

    return dt.replace(fold=fold)