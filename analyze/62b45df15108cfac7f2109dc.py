def status_str(self, prefix=''):
    """
    Devuelve una cadena con el estado del validador, con un prefijo opcional.
    """
    # Asumiendo que el validador tiene atributos como 'is_valid', 'errors', etc.
    status = f"{prefix}Estado del validador:\n"
    status += f"{prefix}  Válido: {self.is_valid}\n"
    if hasattr(self, 'errors'):
        status += f"{prefix}  Errores: {self.errors}\n"
    return status