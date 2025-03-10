def get_silent_args(self, args):
    """
    Lista de argumentos silenciados.

    :param args: Los argumentos recibidos.
    :return: lista, nombres de los argumentos silenciados.
    """
    silent_args = []
    for arg in args:
        if arg.startswith('--'):
            silent_args.append(arg[2:])
    return silent_args