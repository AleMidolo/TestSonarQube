def status_str(self, prefix=''):
    """
    Return string of validator status, with optional prefix.
    """
    status = "Validator Status"
    return f"{prefix}{status}" if prefix else status