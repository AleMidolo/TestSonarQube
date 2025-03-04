def is_none_string(val: any) -> bool:
    """
    Verifica se una stringa rappresenta un valore None.
    """
    return val is None or (isinstance(val, str) and val.lower() == 'none')