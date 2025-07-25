def status_str(self, prefix=''):
    """
    Devuelve una cadena con el estado del validador, con un prefijo opcional.
    """
    # Asumiendo que el validador tiene un atributo 'status' que almacena su estado actual
    return f"{prefix}{self.status}"