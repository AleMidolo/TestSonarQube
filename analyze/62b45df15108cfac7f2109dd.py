def status_str(self, prefix=''):
    """
    Restituisce la rappresentazione in formato stringa del registro di validazione, con un prefisso opzionale.
    """
    return f"{prefix}{self.__dict__}"