def normalized(self):
    """
    Restituisce una versione di questo oggetto rappresentata interamente utilizzando valori interi per gli attributi relativi.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Restituisce un oggetto di tipo :class:`dateutil.relativedelta.relativedelta`.
    """
    from dateutil.relativedelta import relativedelta

    # Convert days to integer and handle the fractional part
    days = int(self.days)
    fractional_days = self.days - days

    # Convert fractional days to hours
    hours = int(fractional_days * 24) + self.hours

    # Handle overflow from hours to days
    extra_days = hours // 24
    days += extra_days
    hours = hours % 24

    # Create a new relativedelta object with integer values
    return relativedelta(days=days, hours=hours, minutes=self.minutes, seconds=self.seconds,
                         microseconds=self.microseconds, years=self.years, months=self.months,
                         leapdays=self.leapdays, year=self.year, month=self.month, day=self.day,
                         weekday=self.weekday, hour=self.hour, minute=self.minute, second=self.second,
                         microsecond=self.microsecond)