def get_nested_custom_and_control_args(self, args):
    """
    Suddivide gli argomenti di input in controlli nidificati e personalizzati.

    Argomenti di controllo: controllano il comportamento dell'IR. Questi argomenti
        non saranno inseriti nel file spec yml.
    Argomenti nidificati: sono utilizzati dai playbook di Ansible e saranno inseriti
        nel file spec yml.
    Argomenti personalizzati: variabili Ansible personalizzate da utilizzare al posto
        dell'uso normale degli argomenti nidificati.

    :param args: la lista raccolta di argomenti.
    :return: (dict, dict): dizionari piatti (control_args, nested_args)
    """
    control_args = {}
    nested_args = {}
    custom_args = {}

    # Iterate through all arguments
    for arg, value in args.items():
        if arg.startswith('--'):
            # Remove leading dashes for control args
            clean_arg = arg.lstrip('-')
            control_args[clean_arg] = value
        elif '__' in arg:
            # Handle nested arguments
            parts = arg.split('__')
            current_dict = nested_args
            
            # Build nested structure
            for part in parts[:-1]:
                if part not in current_dict:
                    current_dict[part] = {}
                current_dict = current_dict[part]
            
            # Set the final value
            current_dict[parts[-1]] = value
        elif arg.startswith('custom_'):
            # Handle custom arguments
            custom_args[arg] = value
        else:
            # Default to nested args
            nested_args[arg] = value

    # Merge custom args into nested args
    nested_args.update(custom_args)

    return control_args, nested_args