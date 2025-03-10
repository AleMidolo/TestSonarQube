def status_str(self, prefix=''):
    """
    Return string representation of validation log, with optional prefix.
    """
    log_entries = []
    for entry in self.log:
        log_entries.append(f"{prefix}{entry}")
    return "\n".join(log_entries)