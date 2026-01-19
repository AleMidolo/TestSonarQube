def get_current_date(self):
    """
    Devuelve la fecha actual en el formato "%Y-%m-%d"
    :return: cadena
    >>> timeutils.get_current_date()
    "2023-06-14"
    """
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")