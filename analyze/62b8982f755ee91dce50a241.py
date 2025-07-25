def normalized(self):
    """
    Return a version of this object represented entirely using integer
    values for the relative attributes.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Returns a :class:`dateutil.relativedelta.relativedelta` object.
    """
    from dateutil.relativedelta import relativedelta
    import math

    # Extract all attributes
    attrs = ['years', 'months', 'days', 'leapdays', 'hours', 'minutes', 'seconds', 'microseconds']
    normalized_attrs = {}

    for attr in attrs:
        value = getattr(self, attr, 0)
        if isinstance(value, float):
            # Convert to integer by rounding down
            normalized_attrs[attr] = int(math.floor(value))
        else:
            normalized_attrs[attr] = value

    # Handle fractional days
    if 'days' in normalized_attrs and isinstance(self.days, float):
        fractional_days = self.days - int(math.floor(self.days))
        hours_from_days = fractional_days * 24
        normalized_attrs['hours'] = normalized_attrs.get('hours', 0) + hours_from_days

    # Handle fractional hours
    if 'hours' in normalized_attrs and isinstance(self.hours, float):
        fractional_hours = self.hours - int(math.floor(self.hours))
        minutes_from_hours = fractional_hours * 60
        normalized_attrs['minutes'] = normalized_attrs.get('minutes', 0) + minutes_from_hours

    # Handle fractional minutes
    if 'minutes' in normalized_attrs and isinstance(self.minutes, float):
        fractional_minutes = self.minutes - int(math.floor(self.minutes))
        seconds_from_minutes = fractional_minutes * 60
        normalized_attrs['seconds'] = normalized_attrs.get('seconds', 0) + seconds_from_minutes

    # Handle fractional seconds
    if 'seconds' in normalized_attrs and isinstance(self.seconds, float):
        fractional_seconds = self.seconds - int(math.floor(self.seconds))
        microseconds_from_seconds = fractional_seconds * 1e6
        normalized_attrs['microseconds'] = normalized_attrs.get('microseconds', 0) + microseconds_from_seconds

    # Create and return the normalized relativedelta object
    return relativedelta(**normalized_attrs)