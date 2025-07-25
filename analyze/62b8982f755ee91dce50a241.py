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

    # Convert days to integer and handle the fractional part
    days = int(self.days)
    fractional_days = self.days - days
    hours = self.hours + fractional_days * 24

    # Convert hours to integer and handle the fractional part
    hours = int(hours)
    fractional_hours = hours - int(hours)
    minutes = self.minutes + fractional_hours * 60

    # Convert minutes to integer and handle the fractional part
    minutes = int(minutes)
    fractional_minutes = minutes - int(minutes)
    seconds = self.seconds + fractional_minutes * 60

    # Convert seconds to integer and handle the fractional part
    seconds = int(seconds)
    fractional_seconds = seconds - int(seconds)
    microseconds = self.microseconds + fractional_seconds * 1e6

    # Create a new relativedelta object with integer values
    return relativedelta(
        years=self.years,
        months=self.months,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=int(microseconds)
    )