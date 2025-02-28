def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Valida y muestra los argumentos obsoletos.

    :param cli_args: el diccionario de argumentos provenientes de la línea de comandos (CLI)
    :param answer_file_args: el diccionario de argumentos provenientes de archivos
    """
    deprecated_args = set(cli_args.keys()).intersection(answer_file_args.keys())
    if deprecated_args:
        print("Advertencia: Los siguientes argumentos están obsoletos y no deberían ser usados:")
        for arg in deprecated_args:
            print(f"- {arg}")
    else:
        print("No se encontraron argumentos obsoletos.")