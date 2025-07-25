def status_str(self, prefix=''):
    """
    Devuelve la representación en forma de cadena del registro de validación, con un prefijo opcional.
    """
    result = []
    if self.errors:
        result.append(f"{prefix}Errores:")
        for error in self.errors:
            result.append(f"{prefix}  {error}")
    
    if self.warnings:
        result.append(f"{prefix}Advertencias:")
        for warning in self.warnings:
            result.append(f"{prefix}  {warning}")
            
    if not result:
        result.append(f"{prefix}Sin errores ni advertencias")
        
    return "\n".join(result)