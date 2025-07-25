def status_str(self, prefix=''):
    """
    Return string of validator status, with optional prefix.
    """
    status = self.status  # Assuming self.status holds the validator's status
    return f"{prefix}{status}"