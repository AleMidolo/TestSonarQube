def normalized(self):
    """
    Restituisce una versione di questo oggetto rappresentata interamente utilizzando valori interi per gli attributi relativi.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Restituisce un oggetto di tipo :class:`dateutil.relativedelta.relativedelta`.
    """
    from dateutil.relativedelta import relativedelta

    # Convert fractional days to hours
    days = int(self.days)
    fractional_days = self.days - days
    hours = self.hours + fractional_days * 24

    # Convert fractional hours to minutes
    hours = int(hours)
    fractional_hours = hours - int(hours)
    minutes = self.minutes + fractional_hours * 60

    # Convert fractional minutes to seconds
    minutes = int(minutes)
    fractional_minutes = minutes - int(minutes)
    seconds = self.seconds + fractional_minutes * 60

    # Convert fractional seconds to microseconds
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
        microseconds=int(microseconds),
        leapdays=self.leapdays,
        year=self.year,
        month=self.month,
        day=self.day,
        weekday=self.weekday,
        hour=self.hour,
        minute=self.minute,
        second=self.second,
        microsecond=int(self.microsecond),
    )