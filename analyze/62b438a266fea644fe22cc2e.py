import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dato un insieme di argomenti della riga di comando con cui è stato invocato questo script, analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser (o "global") a un'istanza di argparse.Namespace.
    """
    # Create the main parser
    main_parser = argparse.ArgumentParser(description="Main parser")
    main_parser.add_argument('--global-arg', type=str, help='Global argument')

    # Create subparsers
    subparsers = main_parser.add_subparsers(dest='subparser_name', help='Sub-commands')

    # Subparser for command 'command1'
    parser_command1 = subparsers.add_parser('command1', help='Command1 help')
    parser_command1.add_argument('--arg1', type=str, help='Argument 1 for command1')

    # Subparser for command 'command2'
    parser_command2 = subparsers.add_parser('command2', help='Command2 help')
    parser_command2.add_argument('--arg2', type=int, help='Argument 2 for command2')

    # Parse the arguments
    parsed_args = main_parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    result = {}
    if parsed_args.subparser_name:
        result[parsed_args.subparser_name] = parsed_args
    else:
        result['global'] = parsed_args

    return result