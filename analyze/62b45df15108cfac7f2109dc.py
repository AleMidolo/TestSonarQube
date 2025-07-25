def status_str(self, prefix=''):
    """
    Return string of validator status, with optional prefix.
    """
    status = self.status  # Assuming `status` is an attribute of the class
    return f"{prefix}{status}"