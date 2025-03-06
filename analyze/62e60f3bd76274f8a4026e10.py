from datetime import timedelta

def dehydrate_timedelta(value):
    """
    Deidratatore per valori di tipo `timedelta`.

    :param value: Un oggetto di tipo `timedelta`.
    :type value: timedelta
    :return: Un dizionario contenente i giorni, secondi e microsecondi del `timedelta`.
    :rtype: dict
    """
    if not isinstance(value, timedelta):
        raise TypeError("Il parametro 'value' deve essere di tipo 'timedelta'.")
    
    return {
        'days': value.days,
        'seconds': value.seconds,
        'microseconds': value.microseconds
    }