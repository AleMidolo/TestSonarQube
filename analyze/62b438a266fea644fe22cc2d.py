def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    Dada una secuencia de argumentos y un diccionario que mapea el nombre de un subparser a una instancia de `argparse.ArgumentParser`, permite que cada subparser solicitado intente analizar todos los argumentos. Esto permite que argumentos comunes como "--repository" sean compartidos entre múltiples subparsers.

    Devuelve el resultado como una tupla que contiene: (un diccionario que mapea el nombre del subparser a un espacio de nombres (`namespace`) de argumentos analizados, una lista de argumentos restantes que no fueron reclamados por ningún subparser).
    """
    parsed_args = {}
    remaining_args = list(unparsed_arguments)
    
    # Iterate through each subparser
    for subparser_name, subparser in subparsers.items():
        try:
            # Try to parse all remaining arguments with current subparser
            namespace, leftover = subparser.parse_known_args(remaining_args)
            
            # Store successfully parsed arguments for this subparser
            parsed_args[subparser_name] = namespace
            
            # Update remaining arguments to only those that weren't parsed
            remaining_args = leftover
            
        except Exception:
            # If parsing fails, continue to next subparser
            continue
            
    return parsed_args, remaining_args