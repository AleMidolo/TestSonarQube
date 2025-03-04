def is_none_string(val: any) -> bool:
    """
    Check if a string represents a None value.
    """
    if isinstance(val, str):
        return val.lower() in ('none', 'null', '')
    return False