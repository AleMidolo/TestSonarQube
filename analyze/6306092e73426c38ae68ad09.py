def validate_length_args(self, args):
    """
    Verifica si el valor de los argumentos no supera la longitud especificada.

    :param args: Los argumentos recibidos.
    """
    for arg in args:
        if isinstance(arg, str) and len(arg) > 255:
            raise ValueError(f"El argumento '{arg}' excede la longitud máxima permitida de 255 caracteres")
        elif isinstance(arg, (list, tuple, dict, set)) and len(arg) > 1000:
            raise ValueError(f"El argumento '{arg}' excede la longitud máxima permitida de 1000 elementos")