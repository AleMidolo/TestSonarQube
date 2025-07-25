def status_str(self, prefix=''):
    """
    Return string of validator status, with optional prefix.
    """
    status = 'valid' if self.is_valid else 'invalid'
    if prefix:
        return f'{prefix}: {status}'
    return status