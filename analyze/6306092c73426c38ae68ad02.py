def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Valida y muestra los argumentos obsoletos.

    :param cli_args: el diccionario de argumentos provenientes de la línea de comandos (CLI)
    :param answer_file_args: el diccionario de argumentos provenientes de archivos
    """
    deprecated_args = {
        'old_arg1': 'Use new_arg1 instead.',
        'old_arg2': 'Use new_arg2 instead.',
        # Add more deprecated arguments as needed
    }

    # Check CLI arguments for deprecation
    for arg in cli_args:
        if arg in deprecated_args:
            print(f"Warning: Argument '{arg}' is deprecated. {deprecated_args[arg]}")

    # Check answer file arguments for deprecation
    for arg in answer_file_args:
        if arg in deprecated_args:
            print(f"Warning: Argument '{arg}' is deprecated. {deprecated_args[arg]}")