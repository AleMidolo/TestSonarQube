import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dado un conjunto de argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como un diccionario que mapea desde el nombre del subparser (o "global") a una instancia de `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser
    parser_a = subparsers.add_parser('command_a', help='Command A help')
    parser_a.add_argument('--arg1', type=int, help='Argument 1 for command A')

    # Another example subparser
    parser_b = subparsers.add_parser('command_b', help='Command B help')
    parser_b.add_argument('--arg2', type=str, help='Argument 2 for command B')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to map subparser names to their respective Namespace objects
    parsed_arguments = {}
    if hasattr(args, 'subparser_name'):
        parsed_arguments[args.subparser_name] = args
    else:
        parsed_arguments['global'] = args

    return parsed_arguments