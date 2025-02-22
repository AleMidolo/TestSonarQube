import datetime

def parse_frequency(frequency):
    """
    Dado un string de frecuencia con un número y una unidad de tiempo, devuelve una instancia correspondiente de 'datetime.timedelta' o 'None' si la frecuencia es 'None' o "always".

    Por ejemplo, dado "3 weeks", devuelve datetime.timedelta(weeks=3).

    Lanza ValueError si la frecuencia proporcionada no puede ser analizada
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
        'weeks': 'weeks',
        'week': 'weeks',
        'months': 'days',  # Approximation: 1 month = 30 days
        'month': 'days',    # Approximation: 1 month = 30 days
        'years': 'days',    # Approximation: 1 year = 365 days
        'year': 'days'      # Approximation: 1 year = 365 days
    }

    parts = frequency.split()
    if len(parts) != 2:
        raise ValueError(f"Cannot parse frequency: {frequency}")

    try:
        value = int(parts[0])
    except ValueError:
        raise ValueError(f"Cannot parse frequency: {frequency}")

    unit = parts[1].lower()
    if unit not in units:
        raise ValueError(f"Cannot parse frequency: {frequency}")

    return datetime.timedelta(**{units[unit]: value})