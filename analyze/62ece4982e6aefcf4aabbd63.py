def is_none_string(val: any) -> bool:
    """
    Verifica si una cadena representa un valor 'None'.
    """
    if isinstance(val, str):
        return val.strip().lower() in ['none', 'null', 'nil', '']
    return val is None