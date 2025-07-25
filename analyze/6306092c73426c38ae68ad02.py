def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Valida y muestra los argumentos obsoletos.

    :param cli_args: el diccionario de argumentos provenientes de la línea de comandos (CLI)
    :param answer_file_args: el diccionario de argumentos provenientes de archivos
    """
    deprecated_args = {
        'force': 'use --yes instead',
        'debug': 'use --verbose instead',
        'quiet': 'use --silent instead'
    }

    # Check CLI arguments
    for arg, replacement in deprecated_args.items():
        if arg in cli_args and cli_args[arg]:
            print(f"Warning: The argument '--{arg}' is deprecated. {replacement}.")

    # Check answer file arguments 
    for arg, replacement in deprecated_args.items():
        if arg in answer_file_args and answer_file_args[arg]:
            print(f"Warning: The argument '{arg}' in the answer file is deprecated. {replacement}.")