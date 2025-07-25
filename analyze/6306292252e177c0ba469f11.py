from datetime import datetime

def format_dt(dt):
    """
    Formatta un oggetto datetime nel modo in cui i nodi D* si aspettano.
    """
    if not isinstance(dt, datetime):
        raise TypeError("L'oggetto fornito non è un'istanza di datetime")
    
    # Formato atteso: YYYY-MM-DDTHH:MM:SS
    return dt.strftime("%Y-%m-%dT%H:%M:%S")