def status_str(self, prefix=''):
    """
    Return string representation of validation log, with optional prefix.
    """
    log_str = ""
    for entry in self.validation_log:
        log_str += f"{prefix}{entry}\n"
    return log_str.strip()