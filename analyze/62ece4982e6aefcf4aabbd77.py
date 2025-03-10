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
    
    try:
        num, unit = frequency.strip().split()
        num = int(num)
    except ValueError:
        raise ValueError(f"Invalid frequency format: {frequency}")
    
    unit = unit.lower()
    if unit in ["second", "seconds", "sec", "s"]:
        return timedelta(seconds=num)
    elif unit in ["minute", "minutes", "min", "m"]:
        return timedelta(minutes=num)
    elif unit in ["hour", "hours", "hr", "h"]:
        return timedelta(hours=num)
    elif unit in ["day", "days", "d"]:
        return timedelta(days=num)
    elif unit in ["week", "weeks", "w"]:
        return timedelta(weeks=num)
    elif unit in ["month", "months", "mon"]:
        return timedelta(days=num * 30)  # Approximate month as 30 days
    elif unit in ["year", "years", "y"]:
        return timedelta(days=num * 365)  # Approximate year as 365 days
    else:
        raise ValueError(f"Unsupported time unit: {unit}")