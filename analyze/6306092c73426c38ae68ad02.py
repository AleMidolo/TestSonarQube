def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Valida e stampa gli argomenti deprecati.

    :param cli_args: il dizionario degli argomenti dalla CLI
    :param answer_file_args: il dizionario degli argomenti dai file
    """
    deprecated_args = set(cli_args.keys()).intersection(answer_file_args.keys())
    
    if deprecated_args:
        print("Attenzione: I seguenti argomenti sono deprecati e non dovrebbero essere usati:")
        for arg in deprecated_args:
            print(f"- {arg}")
    else:
        print("Nessun argomento deprecato trovato.")