from dateutil.relativedelta import relativedelta

def normalized(self):
    """
    Devuelve una versión de este objeto representada completamente utilizando valores enteros para los atributos relativos.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Devuelve un objeto de la clase :class:`dateutil.relativedelta.relativedelta`.
    """
    # Convertir todos los atributos a enteros
    days = int(self.days)
    hours = int(self.hours)
    minutes = int(self.minutes)
    seconds = int(self.seconds)
    microseconds = int(self.microseconds)
    
    # Calcular los valores normalizados
    total_seconds = (self.days - days) * 86400 + (self.hours - hours) * 3600 + (self.minutes - minutes) * 60 + (self.seconds - seconds)
    hours += int(total_seconds // 3600)
    remaining_seconds = total_seconds % 3600
    minutes += int(remaining_seconds // 60)
    seconds += int(remaining_seconds % 60)
    
    # Crear y devolver el nuevo objeto relativedelta
    return relativedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)