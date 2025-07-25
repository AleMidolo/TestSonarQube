def status_str(self, prefix=''):
    """
    Restituisce una stringa che rappresenta lo stato del validatore, con un prefisso opzionale.
    """
    status = f"{prefix}Validator Status: "
    if self.is_valid:
        status += "Valid"
    else:
        status += "Invalid"
    return status