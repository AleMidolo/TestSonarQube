def status_str(self, prefix=''):
    """
    Devuelve la representación en forma de cadena del registro de validación, con un prefijo opcional.
    """
    return f"{prefix}Validation Record: {self.__dict__}"