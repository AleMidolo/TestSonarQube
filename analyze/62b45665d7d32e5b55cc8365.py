import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script, analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser (o "global") a un'istanza di `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Add global arguments
    parser.add_argument('--global-arg', type=str, help='A global argument')
    
    # Create subparsers
    subparsers = parser.add_subparsers(dest='subparser_name', help='Sub-command help')
    
    # Subparser for command 'command1'
    parser_command1 = subparsers.add_parser('command1', help='Command1 help')
    parser_command1.add_argument('--arg1', type=str, help='Argument for command1')
    
    # Subparser for command 'command2'
    parser_command2 = subparsers.add_parser('command2', help='Command2 help')
    parser_command2.add_argument('--arg2', type=int, help='Argument for command2')
    
    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)
    
    # Organize the parsed arguments into a dictionary
    parsed_args = {}
    if hasattr(args, 'subparser_name'):
        parsed_args[args.subparser_name] = args
    else:
        parsed_args['global'] = args
    
    return parsed_args