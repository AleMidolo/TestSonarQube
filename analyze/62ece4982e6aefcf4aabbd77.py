import re
from datetime import timedelta

def parse_frequency(frequency):
    """
    Dato un valore di frequenza sotto forma di stringa contenente un numero e un'unità di tempo,
    restituisci un'istanza corrispondente di datetime.timedelta o None se la frequenza è None o "always".

    Ad esempio, dato "3 weeks", restituisci datetime.timedelta(weeks=3).

    Genera un'eccezione ValueError se la frequenza fornita non può essere analizzata.
    """
    if frequency is None or frequency.lower() == "always":
        return None
    
    pattern = re.compile(r'^(\d+)\s*(second|minute|hour|day|week|month|year)s?$', re.IGNORECASE)
    match = pattern.match(frequency.strip())
    
    if not match:
        raise ValueError(f"Frequenza non valida: {frequency}")
    
    value = int(match.group(1))
    unit = match.group(2).lower()
    
    if unit == "second":
        return timedelta(seconds=value)
    elif unit == "minute":
        return timedelta(minutes=value)
    elif unit == "hour":
        return timedelta(hours=value)
    elif unit == "day":
        return timedelta(days=value)
    elif unit == "week":
        return timedelta(weeks=value)
    elif unit == "month":
        return timedelta(days=value * 30)  # Approximazione
    elif unit == "year":
        return timedelta(days=value * 365)  # Approximazione
    else:
        raise ValueError(f"Unità di tempo non supportata: {unit}")