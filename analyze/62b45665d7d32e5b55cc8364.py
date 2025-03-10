def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    Dada una secuencia de argumentos y un diccionario que mapea el nombre de un subparser a una instancia de `argparse.ArgumentParser`, permite que cada subparser solicitado intente analizar todos los argumentos. Esto permite que argumentos comunes como `--repository` sean compartidos entre múltiples subparsers.

    Devuelve el resultado como una tupla que contiene: 
    - Un diccionario que mapea el nombre del subparser a un espacio de nombres (`namespace`) de argumentos analizados.
    - Una lista de argumentos restantes que no fueron reclamados por ningún subparser.
    """
    parsed_args = {}
    remaining_args = list(unparsed_arguments)
    
    for subparser_name, subparser in subparsers.items():
        try:
            args, remaining = subparser.parse_known_args(remaining_args)
            parsed_args[subparser_name] = args
            remaining_args = remaining
        except SystemExit:
            # Ignore subparsers that fail to parse the arguments
            continue
    
    return parsed_args, remaining_args