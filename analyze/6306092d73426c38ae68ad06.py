def get_silent_args(self, args):
    """
    Lista de argumentos silenciados.

    :param args: Los argumentos recibidos.
    :return: lista, nombres de los argumentos silenciados.
    """
    silent_args = []
    
    for arg in args:
        if arg.startswith('-s') or arg.startswith('--silent'):
            # Remove the -s/--silent prefix to get the argument name
            arg_name = arg.split('=')[0].replace('-s', '').replace('--silent', '').strip('-')
            if arg_name:
                silent_args.append(arg_name)
                
    return silent_args