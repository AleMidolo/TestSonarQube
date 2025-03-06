def status_str(self, prefix=''):
    """
    Devuelve una cadena con el estado del validador, con un prefijo opcional.
    """
    # Asumiendo que el validador tiene atributos que representan su estado
    # Por ejemplo, self.valid, self.errors, etc.
    status = "Válido" if self.valid else "Inválido"
    errors = ", ".join(self.errors) if hasattr(self, 'errors') else "Sin errores"
    
    return f"{prefix}Estado: {status}, Errores: {errors}"