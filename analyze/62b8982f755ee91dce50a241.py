from dateutil.relativedelta import relativedelta

def normalized(self):
    """
    Restituisce una versione di questo oggetto rappresentata interamente utilizzando valori interi per gli attributi relativi.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Restituisce un oggetto di tipo :class:`dateutil.relativedelta.relativedelta`.
    """
    total_hours = int(self.hours) + int(self.days * 24) + int(self.minutes / 60)
    total_days = int(self.days) + (total_hours // 24)
    total_hours = total_hours % 24
    return relativedelta(days=total_days, hours=total_hours, minutes=int(self.minutes % 60), seconds=int(self.seconds))