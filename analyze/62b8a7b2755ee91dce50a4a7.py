from datetime import datetime

def default_tzinfo(dt, tzinfo):
    """
    Establece el parámetro ``tzinfo`` solo en objetos "datetime" que no contienen información de la zona horaria a la que pertenece.

    Esto es útil, por ejemplo, cuando se te proporciona un objeto datetime que puede tener una zona horaria implícita o explícita, como al analizar una cadena de zona horaria.

    :param dt: El objeto datetime al que se le reemplazará la zona horaria.
    :param tzinfo: La instancia de la subclase :py:class:`datetime.tzinfo` que se asignará a ``dt`` si (y solo si) no contienen información de la zona horaria a la que pertenece.
    :return: Devuelve un objeto :py:class:`datetime.datetime` que contienen información de la zona horaria a la que pertenece.
    """
    if dt.tzinfo is None:
        return dt.replace(tzinfo=tzinfo)
    return dt