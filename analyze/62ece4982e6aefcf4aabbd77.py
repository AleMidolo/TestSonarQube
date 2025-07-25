import datetime

def parse_frequency(frequency):
    """
    Dato un valore di frequenza sotto forma di stringa contenente un numero e un'unità di tempo,
    restituisci un'istanza corrispondente di datetime.timedelta o None se la frequenza è None o "always".

    Ad esempio, dato "3 weeks", restituisci datetime.timedelta(weeks=3).

    Genera un'eccezione ValueError se la frequenza fornita non può essere analizzata.
    """
    if frequency is None or frequency.lower() == "always":
        return None

    units = {
        'seconds': 'seconds',
        'second': 'seconds',
        's': 'seconds',
        'minutes': 'minutes',
        'minute': 'minutes',
        'm': 'minutes',
        'hours': 'hours',
        'hour': 'hours',
        'h': 'hours',
        'days': 'days',
        'day': 'days',
        'w': 'weeks',
        'weeks': 'weeks',
        'week': 'weeks',
        'months': 'months',
        'month': 'months',
        'years': 'years',
        'year': 'years'
    }

    parts = frequency.split()
    if len(parts) != 2:
        raise ValueError("Frequency must be in the format '<number> <unit>'")

    try:
        value = int(parts[0])
    except ValueError:
        raise ValueError("The first part of the frequency must be an integer")

    unit = parts[1].lower()
    if unit not in units:
        raise ValueError(f"Unknown time unit: {unit}")

    return datetime.timedelta(**{units[unit]: value})