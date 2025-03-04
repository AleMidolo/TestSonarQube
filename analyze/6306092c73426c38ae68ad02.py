def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Valida e stampa gli argomenti deprecati.

    :param cli_args: il dizionario degli argomenti dalla CLI
    :param answer_file_args: il dizionario degli argomenti dai file
    """
    deprecated_args = {
        'force': 'Use --yes instead',
        'debug': 'Use --verbose instead',
        'quiet': 'Use --silent instead'
    }

    # Check CLI arguments
    for arg, replacement in deprecated_args.items():
        if arg in cli_args and cli_args[arg]:
            print(f"Warning: The argument '--{arg}' is deprecated. {replacement}.")

    # Check answer file arguments 
    for arg, replacement in deprecated_args.items():
        if arg in answer_file_args and answer_file_args[arg]:
            print(f"Warning: The argument '{arg}' in the answer file is deprecated. {replacement}.")