def add_seconds(self, seconds):
    """
        Agrega el número especificado de segundos a la hora actual
        :param seconds: int, número de segundos a agregar
        :return: string, hora después de agregar el número especificado de segundos en el formato '%H:%M:%S'
        >>> timeutils.add_seconds(600)
        "19:29:22"
        """
    new_time = self.datetime + datetime.timedelta(seconds=seconds)
    return new_time.strftime('%H:%M:%S')