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
        # we need to check if the datetime is in the fold
        if dt.fold == 0:
            # If it's the first occurrence, we return it as is
            return new_tz_dt
        else:
            # If it's the second occurrence, we need to adjust
            return new_tz_dt - new_tz_dt.dst()

    return new_tz_dt