def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Valida e stampa gli argomenti deprecati.

    :param cli_args: il dizionario degli argomenti dalla CLI
    :param answer_file_args: il dizionario degli argomenti dai file
    """
    deprecated_args = {
        'old_arg1': 'new_arg1',
        'old_arg2': 'new_arg2',
        # Add more deprecated arguments and their replacements here
    }

    for source_args in [cli_args, answer_file_args]:
        for arg in source_args:
            if arg in deprecated_args:
                print(f"Deprecation Warning: '{arg}' is deprecated. Use '{deprecated_args[arg]}' instead.")