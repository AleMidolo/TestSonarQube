def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Valida e stampa gli argomenti deprecati.

    :param cli_args: il dizionario degli argomenti dalla CLI
    :param answer_file_args: il dizionario degli argomenti dai file
    """
    deprecated_args = set(cli_args.keys()).intersection(answer_file_args.keys())
    
    for arg in deprecated_args:
        print(f"Deprecation Warning: Argument '{arg}' is deprecated and should not be used.")