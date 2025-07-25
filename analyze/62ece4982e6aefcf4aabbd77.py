import datetime

def parse_frequency(frequency):
    """
    Dado un string de frecuencia con un número y una unidad de tiempo, devuelve una instancia correspondiente de 'datetime.timedelta' o 'None' si la frecuencia es 'None' o "always".

    Por ejemplo, dado "3 weeks", devuelve datetime.timedelta(weeks=3).

    Lanza ValueError si la frecuencia proporcionada no puede ser analizada
    """
    if frequency is None or frequency.lower() == "always":
        return None
    
    try:
        num, unit = frequency.strip().split()
        num = int(num)
    except ValueError:
        raise ValueError(f"Frecuencia no válida: {frequency}")
    
    unit = unit.lower()
    if unit in ["second", "seconds", "s"]:
        return datetime.timedelta(seconds=num)
    elif unit in ["minute", "minutes", "m"]:
        return datetime.timedelta(minutes=num)
    elif unit in ["hour", "hours", "h"]:
        return datetime.timedelta(hours=num)
    elif unit in ["day", "days", "d"]:
        return datetime.timedelta(days=num)
    elif unit in ["week", "weeks", "w"]:
        return datetime.timedelta(weeks=num)
    elif unit in ["month", "months"]:
        # Approximate months as 30 days
        return datetime.timedelta(days=num * 30)
    elif unit in ["year", "years", "y"]:
        # Approximate years as 365 days
        return datetime.timedelta(days=num * 365)
    else:
        raise ValueError(f"Unidad de tiempo no válida: {unit}")