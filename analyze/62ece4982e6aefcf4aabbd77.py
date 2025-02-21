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
        "seconds": "seconds",
        "second": "seconds",
        "minutes": "minutes",
        "minute": "minutes",
        "hours": "hours",
        "hour": "hours",
        "days": "days",
        "day": "days",
        "weeks": "weeks",
        "week": "weeks",
        "months": "days",  # Approximation: 1 month = 30 days
        "month": "days",    # Approximation: 1 month = 30 days
        "years": "days",    # Approximation: 1 year = 365 days
        "year": "days"      # Approximation: 1 year = 365 days
    }

    parts = frequency.split()
    if len(parts) != 2:
        raise ValueError("Invalid frequency format")

    try:
        value = int(parts[0])
    except ValueError:
        raise ValueError("Invalid number in frequency")

    unit = parts[1].lower()
    if unit not in units:
        raise ValueError("Invalid time unit in frequency")

    return datetime.timedelta(**{units[unit]: value})