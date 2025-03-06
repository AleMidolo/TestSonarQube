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
        fractional_days = self.days - normalized_attrs['days']
        normalized_attrs['hours'] += int(fractional_days * 24)

    # Handle fractional hours
    if 'hours' in normalized_attrs and isinstance(self.hours, float):
        fractional_hours = self.hours - normalized_attrs['hours']
        normalized_attrs['minutes'] += int(fractional_hours * 60)

    # Handle fractional minutes
    if 'minutes' in normalized_attrs and isinstance(self.minutes, float):
        fractional_minutes = self.minutes - normalized_attrs['minutes']
        normalized_attrs['seconds'] += int(fractional_minutes * 60)

    # Handle fractional seconds
    if 'seconds' in normalized_attrs and isinstance(self.seconds, float):
        fractional_seconds = self.seconds - normalized_attrs['seconds']
        normalized_attrs['microseconds'] += int(fractional_seconds * 1e6)

    return relativedelta(**normalized_attrs)