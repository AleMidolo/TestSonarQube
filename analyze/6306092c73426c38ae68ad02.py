def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Valida e stampa gli argomenti deprecati.

    :param cli_args: il dizionario degli argomenti dalla CLI
    :param answer_file_args: il dizionario degli argomenti dai file
    """
    deprecated_args = {
        'old_arg1': 'new_arg1',
        'old_arg2': 'new_arg2',
        # Aggiungi altri argomenti deprecati qui
    }

    for arg in cli_args:
        if arg in deprecated_args:
            print(f"Attenzione: L'argomento '{arg}' è deprecato. Usa '{deprecated_args[arg]}' invece.")

    for arg in answer_file_args:
        if arg in deprecated_args:
            print(f"Attenzione: L'argomento '{arg}' è deprecato. Usa '{deprecated_args[arg]}' invece.")