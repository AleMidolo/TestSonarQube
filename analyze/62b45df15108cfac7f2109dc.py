def status_str(self, prefix=''):
    """
    Return string of validator status, with optional prefix.
    """
    status = "Valid" if self.is_valid() else "Invalid"
    return f"{prefix}{status}"