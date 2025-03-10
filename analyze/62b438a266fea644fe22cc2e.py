import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y devuélvelos como un diccionario que mapea desde el nombre del subparser (o "global") a una instancia de `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Global arguments
    parser.add_argument('--global-arg', type=str, help="A global argument")

    # Subparser for command 'foo'
    foo_parser = subparsers.add_parser('foo', help="foo command help")
    foo_parser.add_argument('--foo-arg', type=str, help="foo argument")

    # Subparser for command 'bar'
    bar_parser = subparsers.add_parser('bar', help="bar command help")
    bar_parser.add_argument('--bar-arg', type=int, help="bar argument")

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    parsed_args = {}
    if hasattr(args, 'subparser_name'):
        parsed_args[args.subparser_name] = args
    else:
        parsed_args['global'] = args

    return parsed_args