def status_str(self, prefix=''):
    """
    Return string representation of validation log, with optional prefix.
    """
    log_entries = [f"{prefix}{entry}" for entry in self.validation_log]
    return "\n".join(log_entries)