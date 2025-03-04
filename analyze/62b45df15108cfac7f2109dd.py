def status_str(self, prefix=''):
    """
    Devuelve la representación en forma de cadena del registro de validación, con un prefijo opcional.
    """
    result = []
    if hasattr(self, 'validation_errors') and self.validation_errors:
        for error in self.validation_errors:
            result.append(f"{prefix}Error: {error}")
            
    if hasattr(self, 'validation_warnings') and self.validation_warnings:
        for warning in self.validation_warnings:
            result.append(f"{prefix}Warning: {warning}")
            
    if not result:
        result.append(f"{prefix}Valid")
        
    return '\n'.join(result)