def status_str(self, prefix=''):
    """
    Devuelve una cadena con el estado del validador, con un prefijo opcional.
    """
    status = f"{prefix}Estado del validador: "
    if self.is_valid:
        status += "Válido"
    else:
        status += "Inválido"
    return status