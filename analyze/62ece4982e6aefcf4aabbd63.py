def is_none_string(val: any) -> bool:
    """
    Check if a string represents a None value.
    """
    return val == "None" or val is None