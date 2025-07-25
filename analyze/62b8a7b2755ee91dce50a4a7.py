def default_tzinfo(dt, tzinfo):
    """
    Establece el parámetro ``tzinfo`` solo en objetos "datetime" que no contienen información de la zona horaria a la que pertenece.

    Esto es útil, por ejemplo, cuando se te proporciona un objeto datetime que puede tener una zona horaria implícita o explícita, como al analizar una cadena de zona horaria.

    .. doctest::

        >>> from dateutil.tz import tzoffset
        >>> from dateutil.parser import parse
        >>> from dateutil.utils import default_tzinfo
        >>> dflt_tz = tzoffset("EST", -18000)
        >>> print(default_tzinfo(parse('2014-01-01 12:30 UTC'), dflt_tz))
        2014-01-01 12:30:00+00:00
        >>> print(default_tzinfo(parse('2014-01-01 12:30'), dflt_tz))
        2014-01-01 12:30:00-05:00

    :param dt:
        El objeto datetime al que se le reemplazará la zona horaria.

    :param tzinfo:
        La instancia de la subclase :py:class:`datetime.tzinfo` que se asignará a ``dt`` si (y solo si) no contienen información de la zona horaria a la que pertenece.

    :return:
        Devuelve un objeto :py:class:`datetime.datetime` que contienen información de la zona horaria a la que pertenece.
    """
    if dt.tzinfo is None:
        return dt.replace(tzinfo=tzinfo)
    return dt