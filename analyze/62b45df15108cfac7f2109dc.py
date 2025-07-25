def status_str(self, prefix=''):
    """
    Restituisce una stringa che rappresenta lo stato del validatore, con un prefisso opzionale.
    """
    status = []
    if hasattr(self, 'valid'):
        status.append('valid' if self.valid else 'invalid')
    if hasattr(self, 'errors') and self.errors:
        status.append(f'errors={len(self.errors)}')
    if hasattr(self, 'warnings') and self.warnings:
        status.append(f'warnings={len(self.warnings)}')
        
    status_text = ', '.join(status)
    if prefix:
        status_text = f'{prefix}: {status_text}'
        
    return status_text