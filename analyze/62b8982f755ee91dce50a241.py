from dateutil.relativedelta import relativedelta

def normalized(self):
    """
    Restituisce una versione di questo oggetto rappresentata interamente utilizzando valori interi per gli attributi relativi.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Restituisce un oggetto di tipo :class:`dateutil.relativedelta.relativedelta`.
    """
    total_days = int(self.days) + int(self.hours // 24)
    total_hours = int(self.hours % 24)
    return relativedelta(days=total_days, hours=total_hours)