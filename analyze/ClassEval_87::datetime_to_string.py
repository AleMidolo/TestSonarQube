def datetime_to_string(self, datetime):
    """
        Convierte una instancia de datetime a una cadena
        :param datetime: la instancia de datetime a convertir
        :return: cadena, cadena de tiempo convertida
        >>> timeutils.datetime_to_string(timeutils.datetime)
        "2023-06-14 19:30:03"
        """
    format = '%Y-%m-%d %H:%M:%S'
    return datetime.strftime(format)