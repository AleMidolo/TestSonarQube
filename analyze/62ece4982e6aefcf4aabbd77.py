from datetime import timedelta

def parse_frequency(frequency):
    """
    Dado un string de frecuencia con un número y una unidad de tiempo, devuelve una instancia correspondiente de 'datetime.timedelta' o 'None' si la frecuencia es 'None' o "always".

    Por ejemplo, dado "3 weeks", devuelve datetime.timedelta(weeks=3).

    Lanza ValueError si la frecuencia proporcionada no puede ser analizada
    """
    if frequency is None or frequency.lower() == "always":
        return None
    
    try:
        parts = frequency.strip().split()
        if len(parts) != 2:
            raise ValueError("Formato de frecuencia no válido")
        
        num = int(parts[0])
        unit = parts[1].lower()
        
        if unit in ["second", "seconds"]:
            return timedelta(seconds=num)
        elif unit in ["minute", "minutes"]:
            return timedelta(minutes=num)
        elif unit in ["hour", "hours"]:
            return timedelta(hours=num)
        elif unit in ["day", "days"]:
            return timedelta(days=num)
        elif unit in ["week", "weeks"]:
            return timedelta(weeks=num)
        else:
            raise ValueError("Unidad de tiempo no reconocida")
    except (ValueError, IndexError):
        raise ValueError("Frecuencia no puede ser analizada")