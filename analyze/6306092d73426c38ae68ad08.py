def _get_conditionally_required_args(self, command_name, options_spec, args):
    """
    Elenca gli argomenti con la condizione ``required_when`` soddisfatta.

    :param command_name: il nome del comando.
    :param options_spec: la lista delle opzioni specifiche del comando.
    :param args: gli argomenti di input ricevuti.
    :return: list, lista dei nomi degli argomenti con la condizione
        ``required_when`` soddisfatta.
    """
    required_args = []
    
    for option in options_spec:
        if hasattr(option, 'required_when'):
            condition = option.required_when
            if condition(command_name, args):
                required_args.append(option.name)
    
    return required_args