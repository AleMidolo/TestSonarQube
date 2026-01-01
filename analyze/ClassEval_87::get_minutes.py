def get_minutes(self, string_time1, string_time2):
    """
        Calcula cuántos minutos han pasado entre dos tiempos y redondea el resultado al entero más cercano.
        :return: int, el número de minutos entre dos tiempos, redondeado
        >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
        60
        """
    dt1 = self.string_to_datetime(string_time1)
    dt2 = self.string_to_datetime(string_time2)
    time_difference = abs(dt2 - dt1)
    total_seconds = time_difference.total_seconds()
    minutes = total_seconds / 60
    return round(minutes)