from dateutil.relativedelta import relativedelta

def normalized(self):
    """
    Devuelve una versión de este objeto representada completamente utilizando valores enteros para los atributos relativos.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Devuelve un objeto de la clase :class:`dateutil.relativedelta.relativedelta`.
    """
    # Convertir los atributos fraccionarios a enteros
    days = int(self.days)
    hours = int(self.hours)
    minutes = int(self.minutes)
    seconds = int(self.seconds)
    microseconds = int(self.microseconds)

    # Calcular los residuos de las conversiones
    residual_hours = (self.days - days) * 24
    residual_minutes = (self.hours - hours + residual_hours) * 60
    residual_seconds = (self.minutes - minutes + residual_minutes) * 60
    residual_microseconds = (self.seconds - seconds + residual_seconds) * 1_000_000

    # Ajustar los valores de los atributos
    hours += int(residual_hours)
    minutes += int(residual_minutes)
    seconds += int(residual_seconds)
    microseconds += int(residual_microseconds)

    # Asegurarse de que los valores estén dentro de los límites
    minutes += seconds // 60
    seconds %= 60
    hours += minutes // 60
    minutes %= 60
    days += hours // 24
    hours %= 24

    # Crear y devolver el nuevo objeto relativedelta
    return relativedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)