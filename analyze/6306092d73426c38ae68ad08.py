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
            if self._evaluate_condition(condition, args):
                required_args.append(option['name'])
    
    return required_args

def _evaluate_condition(self, condition, args):
    # Implementa la logica per valutare la condizione
    # Restituisce True se la condizione è soddisfatta, altrimenti False
    # Questo è un esempio di implementazione, la logica specifica dipende dai requisiti
    return all(arg in args for arg in condition.get('args', []))