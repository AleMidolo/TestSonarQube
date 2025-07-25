def format_dt(dt):
    """
    Formatta un oggetto datetime nel modo in cui i nodi D* si aspettano.
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")