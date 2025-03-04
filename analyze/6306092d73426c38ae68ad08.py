def _get_conditionally_required_args(self, command_name, options_spec, args):
    """
    Lista los argumentos con la condición ``required_when`` que coincide.

    :param command_name: el nombre del comando.
    :param options_spec: la lista de opciones de especificación del comando.
    :param args: los argumentos de entrada recibidos.
    :return: list, lista de nombres de argumentos que coinciden con la condición ``required_when``.
    """
    conditionally_required = []
    
    for option in options_spec:
        if 'required_when' in option:
            required_condition = option['required_when']
            
            # Evaluar la condición required_when
            if isinstance(required_condition, str):
                # Si es una cadena, evaluar como expresión
                try:
                    condition_met = eval(required_condition, {'args': args})
                except:
                    condition_met = False
            elif callable(required_condition):
                # Si es una función, llamarla con los argumentos
                try:
                    condition_met = required_condition(args)
                except:
                    condition_met = False
            else:
                condition_met = bool(required_condition)
                
            # Si la condición se cumple, agregar el argumento a la lista
            if condition_met:
                conditionally_required.append(option['name'])
                
    return conditionally_required