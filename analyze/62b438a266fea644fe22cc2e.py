import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dato un insieme di argomenti della riga di comando con cui è stato invocato questo script, analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser (o "global") a un'istanza di argparse.Namespace.
    """
    # Create the main parser
    main_parser = argparse.ArgumentParser(description="Main parser")
    subparsers = main_parser.add_subparsers(dest='subparser_name', help='Sub-command help')

    # Global arguments
    main_parser.add_argument('--global-arg', type=str, help='A global argument')

    # Sub-parser 1
    parser1 = subparsers.add_parser('subparser1', help='Subparser 1 help')
    parser1.add_argument('--arg1', type=str, help='Argument for subparser 1')

    # Sub-parser 2
    parser2 = subparsers.add_parser('subparser2', help='Subparser 2 help')
    parser2.add_argument('--arg2', type=int, help='Argument for subparser 2')

    # Parse the arguments
    parsed_args = main_parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    result = {}
    if hasattr(parsed_args, 'subparser_name'):
        result[parsed_args.subparser_name] = parsed_args
    else:
        result['global'] = parsed_args

    return result