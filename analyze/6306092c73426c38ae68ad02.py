def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Valida y muestra los argumentos obsoletos.

    :param cli_args: el diccionario de argumentos provenientes de la línea de comandos (CLI)
    :param answer_file_args: el diccionario de argumentos provenientes de archivos
    """
    deprecated_args = {
        'old_arg1': 'new_arg1',
        'old_arg2': 'new_arg2',
        # Add more deprecated arguments as needed
    }

    for arg in deprecated_args:
        if arg in cli_args:
            print(f"Advertencia: El argumento '{arg}' está obsoleto. Use '{deprecated_args[arg]}' en su lugar.")
        
        if arg in answer_file_args:
            print(f"Advertencia: El argumento '{arg}' está obsoleto en el archivo de respuestas. Use '{deprecated_args[arg]}' en su lugar.")