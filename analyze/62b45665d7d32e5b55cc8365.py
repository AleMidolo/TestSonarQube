import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script, analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser (o "global") a un'istanza di `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(description="Main parser")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser
    parser_a = subparsers.add_parser('subparser_a', help='Subparser A help')
    parser_a.add_argument('--arg1', type=str, help='Argument 1 for subparser A')

    parser_b = subparsers.add_parser('subparser_b', help='Subparser B help')
    parser_b.add_argument('--arg2', type=int, help='Argument 2 for subparser B')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    parsed_args = {}
    if hasattr(args, 'subparser_name'):
        parsed_args[args.subparser_name] = args
    else:
        parsed_args['global'] = args

    return parsed_args