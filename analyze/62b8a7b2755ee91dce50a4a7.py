from datetime import datetime

def default_tzinfo(dt, tzinfo):
    """
    Sets the ``tzinfo`` parameter on naive datetimes only

    This is useful for example when you are provided a datetime that may have
    either an implicit or explicit time zone, such as when parsing a time zone
    string.

    :param dt:
        The datetime on which to replace the time zone

    :param tzinfo:
        The :py:class:`datetime.tzinfo` subclass instance to assign to
        ``dt`` if (and only if) it is naive.

    :return:
        Returns an aware :py:class:`datetime.datetime`.
    """
    if dt.tzinfo is None:
        return dt.replace(tzinfo=tzinfo)
    return dt