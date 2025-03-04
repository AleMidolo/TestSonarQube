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
            condition_met = False
            
            if isinstance(required_condition, dict):
                # Si la condición es un diccionario, verificar que los valores coincidan
                for key, value in required_condition.items():
                    if key in args and args[key] == value:
                        condition_met = True
                    else:
                        condition_met = False
                        break
                        
            elif callable(required_condition):
                # Si la condición es una función, evaluarla
                try:
                    condition_met = required_condition(args)
                except Exception:
                    condition_met = False
                    
            elif isinstance(required_condition, str):
                # Si la condición es un string, evaluar como expresión
                try:
                    # Crear un contexto con los argumentos
                    eval_context = args.copy()
                    condition_met = eval(required_condition, {"__builtins__": {}}, eval_context)
                except Exception:
                    condition_met = False
            
            # Si la condición se cumple, agregar el argumento a la lista
            if condition_met and option.get('name') not in args:
                conditionally_required.append(option.get('name'))
                
    return conditionally_required