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
            
            # Check if required_when is a string (single condition) or list (multiple conditions)
            conditions = [required_when] if isinstance(required_when, str) else required_when
            
            for condition in conditions:
                # Split condition into argument name and expected value
                arg_name, expected_value = condition.split('=')
                arg_name = arg_name.strip()
                expected_value = expected_value.strip()
                
                # Convert expected_value to proper type if needed
                if expected_value.lower() == 'true':
                    expected_value = True
                elif expected_value.lower() == 'false':
                    expected_value = False
                elif expected_value.isdigit():
                    expected_value = int(expected_value)
                
                # Check if the condition matches
                if arg_name in args and args[arg_name] == expected_value:
                    conditionally_required.append(option['name'])
                    break  # Break inner loop if any condition matches
                    
    return conditionally_required