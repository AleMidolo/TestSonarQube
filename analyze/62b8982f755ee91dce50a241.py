def normalized(self):
    """
    Restituisce una versione di questo oggetto rappresentata interamente utilizzando valori interi per gli attributi relativi.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Restituisce un oggetto di tipo :class:`dateutil.relativedelta.relativedelta`.
    """
    # Convert fractional days to hours
    days = int(self.days)
    hours = int((self.days - days) * 24 + self.hours)
    
    # Convert fractional hours to minutes
    extra_hours = int(hours)
    minutes = int((hours - extra_hours) * 60 + self.minutes)
    
    # Convert fractional minutes to seconds
    extra_minutes = int(minutes) 
    seconds = int((minutes - extra_minutes) * 60 + self.seconds)
    
    # Convert fractional seconds to microseconds
    extra_seconds = int(seconds)
    microseconds = int((seconds - extra_seconds) * 1000000 + self.microseconds)

    # Create new relativedelta with normalized values
    return type(self)(
        years=self.years,
        months=self.months,
        days=days,
        hours=extra_hours,
        minutes=extra_minutes,
        seconds=extra_seconds,
        microseconds=microseconds,
        leapdays=self.leapdays,
        year=self.year,
        month=self.month,
        day=self.day,
        weekday=self.weekday,
        hour=self.hour,
        minute=self.minute,
        second=self.second,
        microsecond=self.microsecond
    )