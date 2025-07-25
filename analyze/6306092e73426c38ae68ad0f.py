def get_nested_custom_and_control_args(self, args):
    """
    Divide los argumentos de entrada en controlados, anidados y personalizados.

    Argumentos de control: controlan el comportamiento de IR. Estos argumentos no se incluirán en el archivo spec yml.
    Argumentos anidados: son utilizados por los playbooks de Ansible y se incluirán en el archivo spec yml.
    Argumentos personalizados: Variables personalizadas de Ansible que se usarán en lugar del uso normal de argumentos anidados.

    :param args: la lista recopilada de argumentos.
    :return: (dict, dict): diccionarios planos (control_args, nested_args)
    """
    control_args = {}
    nested_args = {}
    
    for key, value in args.items():
        if key.startswith('control_'):
            control_args[key] = value
        elif key.startswith('nested_'):
            nested_args[key] = value
        else:
            nested_args[key] = value
    
    return control_args, nested_args