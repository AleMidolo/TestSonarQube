def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Valida y muestra los argumentos obsoletos.

    :param cli_args: el diccionario de argumentos provenientes de la línea de comandos (CLI)
    :param answer_file_args: el diccionario de argumentos provenientes de archivos
    """
    deprecated_args = {
        'force': 'use --yes instead',
        'debug': 'use --verbose instead',
        'skip': 'use --exclude instead',
        'quiet': 'use --silent instead'
    }

    # Check CLI arguments
    for arg, value in cli_args.items():
        if arg in deprecated_args and value:
            print(f"Warning: The argument '--{arg}' is deprecated. {deprecated_args[arg]}")

    # Check answer file arguments 
    for arg, value in answer_file_args.items():
        if arg in deprecated_args and value:
            print(f"Warning: The argument '{arg}' in the answer file is deprecated. {deprecated_args[arg]}")