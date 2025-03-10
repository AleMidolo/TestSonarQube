def normalized(self):
    """
    Devuelve una versión de este objeto representada completamente utilizando valores enteros para los atributos relativos.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Devuelve un objeto de la clase :class:`dateutil.relativedelta.relativedelta`.
    """
    from dateutil.relativedelta import relativedelta

    # Convertir días fraccionarios a horas
    days = int(self.days)
    fractional_days = self.days - days
    hours = self.hours + fractional_days * 24

    # Convertir horas fraccionarias a minutos
    hours = int(hours)
    fractional_hours = hours - int(hours)
    minutes = self.minutes + fractional_hours * 60

    # Convertir minutos fraccionarios a segundos
    minutes = int(minutes)
    fractional_minutes = minutes - int(minutes)
    seconds = self.seconds + fractional_minutes * 60

    # Convertir segundos fraccionarios a microsegundos
    seconds = int(seconds)
    fractional_seconds = seconds - int(seconds)
    microseconds = self.microseconds + fractional_seconds * 1e6

    # Crear un nuevo relativedelta con valores enteros
    return relativedelta(
        years=self.years,
        months=self.months,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=microseconds,
        leapdays=self.leapdays,
        year=self.year,
        month=self.month,
        day=self.day,
        weekday=self.weekday,
        hour=self.hour,
        minute=self.minute,
        second=self.second,
        microsecond=self.microsecond
    )