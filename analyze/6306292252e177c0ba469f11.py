from datetime import datetime

def format_dt(dt):
    """
    Formatta un oggetto datetime nel modo in cui i nodi D* si aspettano.
    """
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    
    # Formato atteso dai nodi D*: YYYY-MM-DDTHH:MM:SS
    return dt.strftime("%Y-%m-%dT%H:%M:%S")