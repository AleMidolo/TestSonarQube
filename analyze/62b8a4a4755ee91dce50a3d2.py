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

    # Convert the datetime to the new timezone
    new_dt = dt.astimezone(self)

    # Check if the datetime is in a fold state (ambiguous)
    if new_dt.fold:
        # Handle the ambiguous case (e.g., by choosing the first occurrence)
        new_dt = new_dt.replace(fold=0)

    return new_dt