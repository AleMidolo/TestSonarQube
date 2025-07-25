def status_str(self, prefix=''):
    """
    Devuelve una cadena con el estado del validador, con un prefijo opcional.
    """
    status = []
    if hasattr(self, 'is_valid'):
        status.append('valid' if self.is_valid else 'invalid')
    if hasattr(self, 'errors') and self.errors:
        status.append(f'errors={len(self.errors)}')
    if hasattr(self, 'warnings') and self.warnings:
        status.append(f'warnings={len(self.warnings)}')
        
    status_text = ', '.join(status)
    if not status_text:
        status_text = 'empty'
        
    return f'{prefix}[{status_text}]'