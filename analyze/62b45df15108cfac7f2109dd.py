def status_str(self, prefix=''):
    """
    Return string representation of validation log, with optional prefix.
    """
    output = []
    for status in self.status_log:
        output.append(prefix + str(status))
    return '\n'.join(output)