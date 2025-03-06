def status_str(self, prefix=''):
    """
    Restituisce una stringa che rappresenta lo stato del validatore, con un prefisso opzionale.
    """
    status = f"{prefix}Stato del validatore: "
    if self.is_valid:
        status += "Valido"
    else:
        status += "Non valido"
    return status