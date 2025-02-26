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
    
    for arg in args:
        if isinstance(arg, dict):
            if 'control' in arg:
                control_args.update(arg)
            elif 'nested' in arg:
                nested_args.update(arg)
        else:
            # Assuming custom args are just non-dict items
            control_args[arg] = None

    return control_args, nested_args