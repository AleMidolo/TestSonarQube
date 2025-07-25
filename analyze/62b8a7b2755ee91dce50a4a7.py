def default_tzinfo(dt, tzinfo):
    """
    Imposta il parametro ``tzinfo`` solo sui datetime privi di informazioni sul fuso orario (naive).

    Questo è utile, ad esempio, quando si lavora con un oggetto datetime che può avere un fuso orario implicito o esplicito, come nel caso del parsing di una stringa che rappresenta un fuso orario.

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
        Il datetime su cui sostituire il fuso orario.

    :param tzinfo:
        L'istanza della sottoclasse :py:class:`datetime.tzinfo` da assegnare a
        ``dt`` se (e solo se) è privo di informazioni sul fuso orario (naive).

    :return:
        Restituisce un oggetto :py:class:`datetime.datetime` con informazioni sul fuso orario (aware).
    """
    # Se il datetime è già aware (ha già un tzinfo), lo restituiamo così com'è
    if dt.tzinfo is not None:
        return dt
        
    # Altrimenti, se è naive (non ha tzinfo), gli assegniamo il tzinfo fornito
    return dt.replace(tzinfo=tzinfo)