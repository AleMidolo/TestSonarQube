from datetime import datetime

def format_dt(dt):
    """
    Formatea un objeto `datetime` en el formato que los nodos D* esperan.
    
    Args:
        dt (datetime): Objeto datetime a formatear.
    
    Returns:
        str: Fecha y hora formateada en el formato esperado por los nodos D*.
    """
    return dt.strftime('%Y-%m-%dT%H:%M:%S')