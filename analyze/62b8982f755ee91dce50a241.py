from dateutil.relativedelta import relativedelta

def normalized(self):
    """
    Devuelve una versión de este objeto representada completamente utilizando valores enteros para los atributos relativos.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Devuelve un objeto de la clase :class:`dateutil.relativedelta.relativedelta`.
    """
    total_seconds = self.days * 86400 + self.hours * 3600 + self.minutes * 60 + self.seconds
    days = int(total_seconds // 86400)
    remaining_seconds = total_seconds % 86400
    hours = int(remaining_seconds // 3600)
    remaining_seconds %= 3600
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds % 60)
    
    return relativedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)