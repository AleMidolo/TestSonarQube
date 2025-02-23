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
        if 'required_when' in option:
            condition = option['required_when']
            if self._check_condition(condition, args):
                required_args.append(option['name'])
    
    return required_args

def _check_condition(self, condition, args):
    # Implementa la logica per verificare se la condizione è soddisfatta
    # Questa è una funzione di esempio e dovrebbe essere implementata
    # in base alla logica specifica delle condizioni.
    return True  # Placeholder per la logica di verifica della condizione