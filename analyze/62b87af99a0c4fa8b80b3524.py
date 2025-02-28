def is_run_el(obj):
    """
    Object contains executable method 'run'.
    """
    return callable(getattr(obj, 'run', None))