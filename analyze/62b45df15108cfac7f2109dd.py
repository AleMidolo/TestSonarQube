def status_str(self, prefix=''):
    """
    Restituisce la rappresentazione in formato stringa del registro di validazione, con un prefisso opzionale.
    """
    result = []
    for error in self.errors:
        result.append(f"{prefix}{error}")
    for warning in self.warnings:
        result.append(f"{prefix}{warning}")
    return "\n".join(result) if result else f"{prefix}OK"