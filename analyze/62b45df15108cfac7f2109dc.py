def status_str(self, prefix=''):
    """
    Devuelve una cadena con el estado del validador, con un prefijo opcional.
    """
    # Asumiendo que el validador tiene atributos que representan su estado
    status = f"{prefix}Estado del validador: "
    if hasattr(self, 'is_valid'):
        status += "Válido" if self.is_valid else "Inválido"
    if hasattr(self, 'last_checked'):
        status += f", Última verificación: {self.last_checked}"
    if hasattr(self, 'error_message'):
        status += f", Mensaje de error: {self.error_message}"
    return status