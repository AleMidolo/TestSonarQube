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
    custom_args = {}

    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                if key.startswith('custom_'):
                    custom_args[key] = value
                elif key in ['control_arg1', 'control_arg2']:  # Example control args
                    control_args[key] = value
                else:
                    nested_args[key] = value
        else:
            # Handle non-dict args if necessary
            continue

    return control_args, nested_args