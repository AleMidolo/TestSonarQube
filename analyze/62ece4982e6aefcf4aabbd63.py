def is_none_string(val: any) -> bool:
    """
    Verifica si una cadena representa un valor 'None'.
    """
    if isinstance(val, str):
        return val.lower() in ['none', 'null', 'nil', 'n/a', '']
    return False