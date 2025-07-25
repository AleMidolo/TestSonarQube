import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dado un conjunto de argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como un diccionario que mapea desde el nombre del subparser (o "global") a una instancia de `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Add global arguments
    parser.add_argument('--global-arg', type=str, help='A global argument')
    
    # Create subparsers
    subparsers = parser.add_subparsers(dest='subparser_name', help='Sub-command help')
    
    # Subparser for command 'foo'
    parser_foo = subparsers.add_parser('foo', help='foo help')
    parser_foo.add_argument('--foo-arg', type=int, help='foo argument')
    
    # Subparser for command 'bar'
    parser_bar = subparsers.add_parser('bar', help='bar help')
    parser_bar.add_argument('--bar-arg', type=float, help='bar argument')
    
    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)
    
    # Organize arguments into a dictionary
    parsed_args = {}
    if hasattr(args, 'subparser_name'):
        parsed_args[args.subparser_name] = args
    else:
        parsed_args['global'] = args
    
    return parsed_args