def status_str(self, prefix=''):
    """
    Return string representation of validation log, with optional prefix.
    """
    log_entries = self.get_validation_log()  # Assuming this method exists to get the log entries
    log_str = "\n".join([f"{prefix}{entry}" for entry in log_entries])
    return log_str