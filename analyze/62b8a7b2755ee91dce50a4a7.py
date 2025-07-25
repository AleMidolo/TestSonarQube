from datetime import datetime

def default_tzinfo(dt, tzinfo):
    """
    Imposta il parametro ``tzinfo`` solo sui datetime privi di informazioni sul fuso orario (naive).

    :param dt: Il datetime su cui sostituire il fuso orario.
    :param tzinfo: L'istanza della sottoclasse :py:class:`datetime.tzinfo` da assegnare a ``dt`` se (e solo se) è privo di informazioni sul fuso orario (naive).
    :return: Restituisce un oggetto :py:class:`datetime.datetime` con informazioni sul fuso orario (aware).
    """
    if dt.tzinfo is None:
        return dt.replace(tzinfo=tzinfo)
    return dt