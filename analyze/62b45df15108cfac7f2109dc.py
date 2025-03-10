def status_str(self, prefix=''):
    """
    Restituisce una stringa che rappresenta lo stato del validatore, con un prefisso opzionale.
    """
    status = "Valid" if self.is_valid() else "Invalid"
    return f"{prefix}{status}"