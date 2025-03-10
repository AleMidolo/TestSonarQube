def is_none_string(val: any) -> bool:
    """
    Check if a string represents a None value.
    """
    if isinstance(val, str):
        return val.lower() in ('none', 'null', 'nil', '')
    return val is None