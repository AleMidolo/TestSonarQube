def get_current_time(self):
    """
    Restituisce l'ora corrente nel formato '%H:%M:%S'
    :return: stringa
    >>> timeutils = TimeUtils()
    >>> timeutils.get_current_time()
    "19:19:22"
    """
    from datetime import datetime
    return datetime.now().strftime('%H:%M:%S')