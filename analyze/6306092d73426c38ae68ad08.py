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
                # Si es string, verificar si el argumento mencionado existe
                if required_condition in args and args[required_condition]:
                    conditionally_required.append(option['name'])
            elif isinstance(required_condition, dict):
                # Si es diccionario, evaluar la condición compleja
                matches = True
                for key, value in required_condition.items():
                    if key not in args or args[key] != value:
                        matches = False
                        break
                if matches:
                    conditionally_required.append(option['name'])
            elif callable(required_condition):
                # Si es una función, evaluarla
                if required_condition(args):
                    conditionally_required.append(option['name'])
                    
    return conditionally_required