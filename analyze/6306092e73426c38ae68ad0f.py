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
    
    for key, value in args.items():
        if key.startswith('control_'):
            control_args[key] = value
        elif key.startswith('nested_'):
            nested_args[key] = value
        else:
            nested_args[key] = value  # Assume custom args are nested by default
    
    return control_args, nested_args