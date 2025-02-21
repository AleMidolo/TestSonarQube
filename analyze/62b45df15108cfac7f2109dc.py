def status_str(self, prefix=''):
    """
    Restituisce una stringa che rappresenta lo stato del validatore, con un prefisso opzionale.
    """
    status = "Validatore attivo" if self.is_active else "Validatore inattivo"
    return f"{prefix}{status}"