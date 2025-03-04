def get_nested_custom_and_control_args(self, args):
    """
    Divide los argumentos de entrada en controlados, anidados y personalizados.

    Argumentos de control: controlan el comportamiento de IR. Estos argumentos no se incluirán en el archivo spec yml.
    Argumentos anidados: son utilizados por los playbooks de Ansible y se incluirán en el archivo spec yml.
    Argumentos personalizados: Variables personalizadas de Ansible que se usarán en lugar del uso normal de argumentos anidados.

    :param args: la lista recopilada de argumentos.
    :return: (dict, dict): diccionarios planos (control_args, nested_args)
    """
    # Initialize result dictionaries
    control_args = {}
    nested_args = {}
    custom_args = {}

    # Iterate through all arguments
    for arg_name, arg_value in args.items():
        if arg_name.startswith('--'):
            # Control arguments start with '--'
            clean_name = arg_name[2:]
            control_args[clean_name] = arg_value
        elif '__' in arg_name:
            # Nested arguments contain '__'
            parent, child = arg_name.split('__', 1)
            if parent not in nested_args:
                nested_args[parent] = {}
            nested_args[parent][child] = arg_value
        elif arg_name.startswith('custom_'):
            # Custom arguments start with 'custom_'
            custom_args[arg_name] = arg_value
        else:
            # Regular nested arguments
            nested_args[arg_name] = arg_value

    # Merge custom args into nested args
    if custom_args:
        nested_args['custom'] = custom_args

    return control_args, nested_args