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

    # Convert all attributes to integers
    days = int(self.days)
    hours = int(self.hours)
    minutes = int(self.minutes)
    seconds = int(self.seconds)
    microseconds = int(self.microseconds)

    # Handle fractional parts
    fractional_days = self.days - days
    fractional_hours = self.hours - hours
    fractional_minutes = self.minutes - minutes
    fractional_seconds = self.seconds - seconds
    fractional_microseconds = self.microseconds - microseconds

    # Convert fractional parts to lower units
    hours += int(fractional_days * 24)
    minutes += int(fractional_hours * 60)
    seconds += int(fractional_minutes * 60)
    microseconds += int(fractional_seconds * 1e6)

    # Normalize the time components
    seconds += microseconds // 1000000
    microseconds = microseconds % 1000000
    minutes += seconds // 60
    seconds = seconds % 60
    hours += minutes // 60
    minutes = minutes % 60
    days += hours // 24
    hours = hours % 24

    return relativedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)