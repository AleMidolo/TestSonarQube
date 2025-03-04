def is_none_string(val: any) -> bool:
    """
    Verifica se una stringa rappresenta un valore None.
    """
    if isinstance(val, str):
        return val.lower() in ['none', 'null', '']
    return val is None