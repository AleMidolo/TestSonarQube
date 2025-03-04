def status_str(self, prefix=''):
    """
    Return string representation of validation log, with optional prefix.
    """
    output = []
    for entry in self.log:
        if entry.get('status') == 'error':
            output.append(f"{prefix}ERROR: {entry.get('message')}")
        elif entry.get('status') == 'warning': 
            output.append(f"{prefix}WARNING: {entry.get('message')}")
        else:
            output.append(f"{prefix}{entry.get('message')}")
    return '\n'.join(output)