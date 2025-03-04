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
            # Control arguments start with --
            control_args[arg[2:]] = value
        elif '__' in arg:
            # Nested arguments contain __
            keys = arg.split('__')
            current_dict = nested_args
            
            # Build nested dictionary structure
            for key in keys[:-1]:
                if key not in current_dict:
                    current_dict[key] = {}
                current_dict = current_dict[key]
            
            # Set the final value
            current_dict[keys[-1]] = value
        else:
            # Custom arguments are everything else
            custom_args[arg] = value

    # Merge custom args into nested args
    nested_args.update(custom_args)

    return control_args, nested_args