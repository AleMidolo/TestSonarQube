def status_str(self, prefix=''):
    """
    Return string representation of validation log, with optional prefix.
    """
    output = []
    for entry in self.log:
        if entry.status == 'pass':
            status = '���'
        elif entry.status == 'fail': 
            status = '���'
        elif entry.status == 'warn':
            status = '!'
        else:
            status = '?'
            
        msg = f"{prefix}{status} {entry.message}"
        if entry.details:
            msg += f" ({entry.details})"
            
        output.append(msg)
        
    return '\n'.join(output)