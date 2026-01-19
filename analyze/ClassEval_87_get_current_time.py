def get_current_time(self):
    """
    Devuelve la hora actual en el formato '%H:%M:%S'
    :return: cadena
    >>> timeutils = TimeUtils()
    >>> timeutils.get_current_time()
    "19:19:22"
    """
    from datetime import datetime
    return datetime.now().strftime('%H:%M:%S')