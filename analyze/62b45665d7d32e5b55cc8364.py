def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    Dada una secuencia de argumentos y un diccionario que mapea el nombre de un subparser a una instancia de `argparse.ArgumentParser`, permite que cada subparser solicitado intente analizar todos los argumentos. Esto permite que argumentos comunes como `--repository` sean compartidos entre múltiples subparsers.

    Devuelve el resultado como una tupla que contiene: 
    - Un diccionario que mapea el nombre del subparser a un espacio de nombres (`namespace`) de argumentos analizados.
    - Una lista de argumentos restantes que no fueron reclamados por ningún subparser.
    """
    parsed_args = {}
    remaining_args = list(unparsed_arguments)

    # Try each subparser
    for name, subparser in subparsers.items():
        try:
            # Parse known args, allowing unknown ones
            namespace, unknown = subparser.parse_known_args(remaining_args)
            parsed_args[name] = namespace
            
            # Update remaining args to only those that weren't parsed
            remaining_args = unknown
            
        except SystemExit:
            # Skip if parsing fails for this subparser
            continue
            
    return parsed_args, remaining_args