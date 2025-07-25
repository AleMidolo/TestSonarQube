def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    Dada una secuencia de argumentos y un diccionario que mapea el nombre de un subparser a una instancia de `argparse.ArgumentParser`, permite que cada subparser solicitado intente analizar todos los argumentos. Esto permite que argumentos comunes como `--repository` sean compartidos entre múltiples subparsers.

    Devuelve el resultado como una tupla que contiene: 
    - Un diccionario que mapea el nombre del subparser a un espacio de nombres (`namespace`) de argumentos analizados.
    - Una lista de argumentos restantes que no fueron reclamados por ningún subparser.
    """
    results = {}
    remaining_arguments = unparsed_arguments[:]
    
    for name, parser in subparsers.items():
        # Try to parse the arguments for the current subparser
        try:
            # Parse the arguments for the current subparser
            parsed_args, remaining_arguments = parser.parse_known_args(remaining_arguments)
            results[name] = parsed_args
        except SystemExit:
            # If parsing fails, we can skip this subparser
            continue
    
    return results, remaining_arguments