def status_str(self, prefix=''):
    """
    Return string representation of validation log, with optional prefix.
    """
    output = []
    for entry in self.log:
        if isinstance(entry, str):
            output.append(prefix + entry)
        else:
            status, msg = entry
            if status:
                output.append(prefix + "��� " + msg)
            else:
                output.append(prefix + "��� " + msg)
    return "\n".join(output)