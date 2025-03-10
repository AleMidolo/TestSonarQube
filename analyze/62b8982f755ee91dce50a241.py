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
    total_hours = self.hours + (self.days % 1) * 24
    days = int(self.days)
    hours = int(total_hours)

    # Handle overflow from hours to days
    if hours >= 24:
        days += hours // 24
        hours = hours % 24

    return relativedelta(days=days, hours=hours)