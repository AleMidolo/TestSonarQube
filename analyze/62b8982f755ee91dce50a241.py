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
    total_hours = int(self.days * 24) + self.hours
    days = total_hours // 24
    hours = total_hours % 24

    # Create a new relativedelta object with integer values
    return relativedelta(days=days, hours=hours, minutes=self.minutes, seconds=self.seconds,
                         microseconds=self.microseconds, years=self.years, months=self.months)