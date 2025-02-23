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
            if 'control' in arg:
                control_args.update(arg)
            elif 'nested' in arg:
                nested_args.update(arg)
            elif 'custom' in arg:
                custom_args.update(arg)

    return control_args, {**nested_args, **custom_args}