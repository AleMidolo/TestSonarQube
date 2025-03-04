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
            required_when = option['required_when']
            
            # Check if required_when is a string (single condition) or dict (multiple conditions)
            if isinstance(required_when, str):
                # Single condition case
                if args.get(required_when):
                    conditionally_required.append(option['name'])
            elif isinstance(required_when, dict):
                # Multiple conditions case
                all_conditions_met = True
                for key, value in required_when.items():
                    if args.get(key) != value:
                        all_conditions_met = False
                        break
                if all_conditions_met:
                    conditionally_required.append(option['name'])
                    
    return conditionally_required