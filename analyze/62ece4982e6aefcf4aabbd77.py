import re
from datetime import timedelta

def parse_frequency(frequency):
    """
    Dado un string de frecuencia con un número y una unidad de tiempo, devuelve una instancia correspondiente de 'datetime.timedelta' o 'None' si la frecuencia es 'None' o "always".

    Por ejemplo, dado "3 weeks", devuelve datetime.timedelta(weeks=3).

    Lanza ValueError si la frecuencia proporcionada no puede ser analizada
    """
    if frequency is None or frequency.lower() == "always":
        return None
    
    pattern = re.compile(r'^(\d+)\s*(second|minute|hour|day|week|month|year)s?$', re.IGNORECASE)
    match = pattern.match(frequency.strip())
    
    if not match:
        raise ValueError(f"Frecuencia no válida: {frequency}")
    
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
        return timedelta(days=value * 30)  # Aproximación de 30 días por mes
    elif unit == "year":
        return timedelta(days=value * 365)  # Aproximación de 365 días por año
    else:
        raise ValueError(f"Unidad de tiempo no válida: {unit}")