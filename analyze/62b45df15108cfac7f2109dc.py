def status_str(self, prefix=''):
    """
    Devuelve una cadena con el estado del validador, con un prefijo opcional.
    """
    # Asumiendo que el validador tiene atributos como 'is_valid', 'errors', etc.
    status = "Valid" if self.is_valid else "Invalid"
    error_msg = f", Errors: {self.errors}" if hasattr(self, 'errors') and self.errors else ""
    return f"{prefix}{status}{error_msg}"