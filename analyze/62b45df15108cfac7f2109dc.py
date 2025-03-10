def status_str(self, prefix=''):
    """
    Restituisce una stringa che rappresenta lo stato del validatore, con un prefisso opzionale.
    """
    status = f"{prefix}Stato del validatore: "
    if hasattr(self, 'is_valid'):
        status += "Valido" if self.is_valid else "Non valido"
    else:
        status += "Stato sconosciuto"
    return status