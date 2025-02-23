def status_str(self, prefix=''):
    """
    Restituisce una stringa che rappresenta lo stato del validatore, con un prefisso opzionale.
    """
    # Assuming 'self' has an attribute 'status' that holds the current status of the validator
    return f"{prefix}{self.status}"