def status_str(self, prefix=''):
    """
    Return string of validator status, with optional prefix.
    """
    status = self.get_status()  # Assuming get_status() is a method that returns the validator's status
    return f"{prefix}{status}"