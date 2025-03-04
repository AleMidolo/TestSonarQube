def _get_conditionally_required_args(self, command_name, options_spec, args):
    """
    Elenca gli argomenti con la condizione ``required_when`` soddisfatta.

    :param command_name: il nome del comando.
    :param options_spec: la lista delle opzioni specifiche del comando.
    :param args: gli argomenti di input ricevuti.
    :return: list, lista dei nomi degli argomenti con la condizione
        ``required_when`` soddisfatta.
    """
    conditionally_required = []
    
    for option in options_spec:
        if 'required_when' in option:
            condition = option['required_when']
            
            # Evaluate the condition based on the args
            if isinstance(condition, str):
                # Simple condition checking if another arg is present
                if condition in args and option['name'] not in args:
                    conditionally_required.append(option['name'])
            
            elif callable(condition):
                # Complex condition using a function
                if condition(args) and option['name'] not in args:
                    conditionally_required.append(option['name'])
                    
            elif isinstance(condition, dict):
                # Dictionary condition checking arg values
                all_conditions_met = True
                for arg_name, expected_value in condition.items():
                    if arg_name not in args or args[arg_name] != expected_value:
                        all_conditions_met = False
                        break
                
                if all_conditions_met and option['name'] not in args:
                    conditionally_required.append(option['name'])
    
    return conditionally_required