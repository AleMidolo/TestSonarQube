from dateutil.relativedelta import relativedelta

def normalized(self):
    """
    Devuelve una versión de este objeto representada completamente utilizando valores enteros para los atributos relativos.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Devuelve un objeto de la clase :class:`dateutil.relativedelta.relativedelta`.
    """
    total_days = int(self.days) + int(self.hours // 24)
    total_hours = int(self.hours % 24)
    
    return relativedelta(days=total_days, hours=total_hours)