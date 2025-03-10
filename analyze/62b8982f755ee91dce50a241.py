def normalized(self):
    """
    Restituisce una versione di questo oggetto rappresentata interamente utilizzando valori interi per gli attributi relativi.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Restituisce un oggetto di tipo :class:`dateutil.relativedelta.relativedelta`.
    """
    from dateutil.relativedelta import relativedelta

    # Convert days to integer and handle fractional days
    days = int(self.days)
    remaining_hours = (self.days - days) * 24

    # Convert hours to integer and handle fractional hours
    hours = int(self.hours + remaining_hours)
    remaining_minutes = (self.hours + remaining_hours - hours) * 60

    # Convert minutes to integer and handle fractional minutes
    minutes = int(self.minutes + remaining_minutes)
    remaining_seconds = (self.minutes + remaining_minutes - minutes) * 60

    # Convert seconds to integer and handle fractional seconds
    seconds = int(self.seconds + remaining_seconds)
    remaining_microseconds = (self.seconds + remaining_seconds - seconds) * 1e6

    # Convert microseconds to integer
    microseconds = int(self.microseconds + remaining_microseconds)

    # Create a new relativedelta object with integer values
    return relativedelta(
        years=self.years,
        months=self.months,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=microseconds,
        leapdays=self.leapdays,
        year=self.year,
        month=self.month,
        day=self.day,
        hour=self.hour,
        minute=self.minute,
        second=self.second,
        microsecond=self.microsecond
    )