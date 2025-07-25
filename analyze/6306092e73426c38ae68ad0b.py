def validate_min_max_args(self, args):
    """
    Verifica si el valor de los argumentos está entre los valores mínimo y máximo.

    :param args: Los argumentos recibidos.
    """
    min_value = self.min_value  # Suponiendo que min_value es un atributo de la clase
    max_value = self.max_value  # Suponiendo que max_value es un atributo de la clase

    for arg in args:
        if not (min_value <= arg <= max_value):
            return False
    return True