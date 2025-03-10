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
    
    pattern = re.compile(r'^(\d+)\s*(seconds?|minutes?|hours?|days?|weeks?)$', re.IGNORECASE)
    match = pattern.match(frequency.strip())
    
    if not match:
        raise ValueError(f"Frecuencia no válida: {frequency}")
    
    value = int(match.group(1))
    unit = match.group(2).lower()
    
    if unit.startswith('second'):
        return timedelta(seconds=value)
    elif unit.startswith('minute'):
        return timedelta(minutes=value)
    elif unit.startswith('hour'):
        return timedelta(hours=value)
    elif unit.startswith('day'):
        return timedelta(days=value)
    elif unit.startswith('week'):
        return timedelta(weeks=value)
    else:
        raise ValueError(f"Unidad de tiempo no reconocida: {unit}")