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
    months = int(self.months)
    years = int(self.years)

    # Ajustar los valores para que estén en el rango correcto
    # Por ejemplo, si hay fracciones de días, convertirlas a horas, etc.
    extra_hours = int((self.days - days) * 24)
    hours += extra_hours

    extra_minutes = int((self.hours - int(self.hours)) * 60
    minutes += extra_minutes

    extra_seconds = int((self.minutes - int(self.minutes)) * 60)
    seconds += extra_seconds

    extra_microseconds = int((self.seconds - int(self.seconds)) * 1e6)
    microseconds += extra_microseconds

    # Crear un nuevo objeto relativedelta con los valores normalizados
    return relativedelta(days=days, hours=hours, minutes=minutes, seconds=seconds,
                         microseconds=microseconds, months=months, years=years)