import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y devuélvelos como un diccionario que mapea desde el nombre del subparser (o "global") a una instancia de `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Add global arguments
    parser.add_argument('--global-arg', type=str, help='A global argument')
    
    # Create subparsers
    subparsers = parser.add_subparsers(dest='subparser_name', help='Sub-command help')
    
    # Subparser for command 'command1'
    parser_command1 = subparsers.add_parser('command1', help='Command1 help')
    parser_command1.add_argument('--arg1', type=str, help='Argument 1 for command1')
    
    # Subparser for command 'command2'
    parser_command2 = subparsers.add_parser('command2', help='Command2 help')
    parser_command2.add_argument('--arg2', type=str, help='Argument 2 for command2')
    
    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)
    
    # Organize the arguments into a dictionary
    parsed_arguments = {}
    if hasattr(args, 'subparser_name'):
        parsed_arguments[args.subparser_name] = args
    else:
        parsed_arguments['global'] = args
    
    return parsed_arguments