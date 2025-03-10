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

    # Calcular los residuos y ajustar los valores
    hours += int((self.days - days) * 24)
    minutes += int((self.hours - int(self.hours)) * 60)
    seconds += int((self.minutes - int(self.minutes)) * 60)
    microseconds += int((self.seconds - int(self.seconds)) * 1e6)

    # Asegurarse de que los valores estén dentro de los límites
    minutes += seconds // 60
    seconds %= 60
    hours += minutes // 60
    minutes %= 60
    days += hours // 24
    hours %= 24

    # Crear y devolver el nuevo objeto relativedelta normalizado
    return relativedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)