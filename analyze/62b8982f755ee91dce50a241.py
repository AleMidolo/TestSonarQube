def normalized(self):
    """
    Devuelve una versión de este objeto representada completamente utilizando valores enteros para los atributos relativos.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Devuelve un objeto de la clase :class:`dateutil.relativedelta.relativedelta`.
    """
    # Convertir días fraccionarios a horas
    days = int(self.days)
    hours_from_days = (self.days - days) * 24
    total_hours = self.hours + hours_from_days
    
    # Convertir horas fraccionarias a minutos
    hours = int(total_hours)
    minutes_from_hours = (total_hours - hours) * 60
    total_minutes = self.minutes + minutes_from_hours
    
    # Convertir minutos fraccionarios a segundos
    minutes = int(total_minutes)
    seconds_from_minutes = (total_minutes - minutes) * 60
    total_seconds = self.seconds + seconds_from_minutes
    
    # Convertir segundos fraccionarios a microsegundos
    seconds = int(total_seconds)
    microseconds = int((total_seconds - seconds) * 1000000) + self.microseconds
    
    # Crear nuevo objeto relativedelta con valores normalizados
    return self.__class__(years=self.years, months=self.months,
                         days=days, hours=hours,
                         minutes=minutes, seconds=seconds,
                         microseconds=microseconds,
                         leapdays=self.leapdays,
                         year=self.year, month=self.month,
                         day=self.day, weekday=self.weekday,
                         hour=self.hour, minute=self.minute,
                         second=self.second, microsecond=self.microsecond)