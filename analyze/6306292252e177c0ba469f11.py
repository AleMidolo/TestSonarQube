from datetime import datetime

def format_dt(dt):
    """
    Formatea un objeto `datetime` en el formato que los nodos D* esperan.
    """
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')