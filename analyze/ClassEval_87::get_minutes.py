def get_minutes(self, string_time1, string_time2):
    """
    Calcula cuántos minutos han pasado entre dos tiempos y redondea el resultado al entero más cercano.
    :return: int, el número de minutos entre dos tiempos, redondeado
    >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
    60
    """
    dt1 = datetime.datetime.strptime(string_time1, '%Y-%m-%d %H:%M:%S')
    dt2 = datetime.datetime.strptime(string_time2, '%Y-%m-%d %H:%M:%S')
    delta = dt2 - dt1
    return round(delta.total_seconds() / 60)