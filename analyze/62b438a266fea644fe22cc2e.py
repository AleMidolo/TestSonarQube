import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dato un insieme di argomenti della riga di comando con cui è stato invocato questo script, analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser (o "global") a un'istanza di argparse.Namespace.
    """
    # Create the main parser
    main_parser = argparse.ArgumentParser(description="Main parser")
    subparsers = main_parser.add_subparsers(dest='subparser_name', help='sub-command help')

    # Example subparser 1
    parser_a = subparsers.add_parser('command_a', help='command_a help')
    parser_a.add_argument('--arg1', type=int, help='arg1 help')
    parser_a.add_argument('--arg2', type=str, help='arg2 help')

    # Example subparser 2
    parser_b = subparsers.add_parser('command_b', help='command_b help')
    parser_b.add_argument('--arg3', type=float, help='arg3 help')
    parser_b.add_argument('--arg4', type=str, help='arg4 help')

    # Parse the arguments
    parsed_args = main_parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    result = {}
    if parsed_args.subparser_name:
        result[parsed_args.subparser_name] = parsed_args
    else:
        result['global'] = parsed_args

    return result