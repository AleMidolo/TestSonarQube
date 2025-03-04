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
        # Check if argument is a control argument (starts with '--')
        if arg.startswith('--'):
            control_args[arg.lstrip('-')] = value
        # Check if argument is a custom argument (contains '=')
        elif '=' in arg:
            key, val = arg.split('=', 1)
            custom_args[key] = val
        # Otherwise it's a nested argument
        else:
            nested_path = arg.split('.')
            current_dict = nested_args
            
            # Build nested dictionary structure
            for part in nested_path[:-1]:
                if part not in current_dict:
                    current_dict[part] = {}
                current_dict = current_dict[part]
            
            # Set the final value
            current_dict[nested_path[-1]] = value

    # Merge custom args into nested args, overwriting any conflicts
    nested_args.update(custom_args)

    return control_args, nested_args