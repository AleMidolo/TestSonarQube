def add_seconds(self, seconds):
    """
    Agrega el número especificado de segundos a la hora actual
    :param seconds: int, número de segundos a agregar
    :return: string, hora después de agregar el número especificado de segundos en el formato '%H:%M:%S'
    >>> timeutils.add_seconds(600)
    "19:29:22"
    """
    from datetime import datetime, timedelta
    
    current_time = datetime.now()
    new_time = current_time + timedelta(seconds=seconds)
    return new_time.strftime('%H:%M:%S')