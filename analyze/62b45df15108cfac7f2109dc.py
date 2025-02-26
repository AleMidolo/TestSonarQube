def status_str(self, prefix=''):
    """
    Return string of validator status, with optional prefix.
    """
    status = "Validator is active" if self.is_active else "Validator is inactive"
    return f"{prefix}{status}"