def normalized(self):
    """
    Devuelve una versión de este objeto representada completamente utilizando valores enteros para los atributos relativos.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Devuelve un objeto de la clase :class:`dateutil.relativedelta.relativedelta`.
    """
    from dateutil.relativedelta import relativedelta
    import math

    # Convertir días fraccionarios a horas
    days_fractional, days_integer = math.modf(self.days)
    hours_from_days = days_fractional * 24

    # Sumar las horas fraccionarias de los días a las horas existentes
    total_hours = self.hours + hours_from_days

    # Convertir horas fraccionarias a minutos
    hours_fractional, hours_integer = math.modf(total_hours)
    minutes_from_hours = hours_fractional * 60

    # Sumar los minutos fraccionarios de las horas a los minutos existentes
    total_minutes = self.minutes + minutes_from_hours

    # Convertir minutos fraccionarios a segundos
    minutes_fractional, minutes_integer = math.modf(total_minutes)
    seconds_from_minutes = minutes_fractional * 60

    # Sumar los segundos fraccionarios de los minutos a los segundos existentes
    total_seconds = self.seconds + seconds_from_minutes

    # Convertir segundos fraccionarios a microsegundos
    seconds_fractional, seconds_integer = math.modf(total_seconds)
    microseconds_from_seconds = seconds_fractional * 1e6

    # Sumar los microsegundos fraccionarios de los segundos a los microsegundos existentes
    total_microseconds = self.microseconds + microseconds_from_seconds

    # Crear un nuevo relativedelta con valores enteros
    return relativedelta(
        years=self.years,
        months=self.months,
        days=int(days_integer),
        hours=int(hours_integer),
        minutes=int(minutes_integer),
        seconds=int(seconds_integer),
        microseconds=int(total_microseconds),
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