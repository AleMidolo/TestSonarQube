def _get_conditionally_required_args(self, command_name, options_spec, args):
    """
    Lista los argumentos con la condición ``required_when`` que coincide.

    :param command_name: el nombre del comando.
    :param options_spec: la lista de opciones de especificación del comando.
    :param args: los argumentos de entrada recibidos.
    :return: list, lista de nombres de argumentos que coinciden con la condición ``required_when``.
    """
    required_args = []
    for option in options_spec:
        if 'required_when' in option:
            condition = option['required_when']
            if condition(command_name, args):
                required_args.append(option['name'])
    return required_args