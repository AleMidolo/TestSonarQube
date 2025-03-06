import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script, analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser (o "global") a un'istanza di `argparse.Namespace`.
    """
    # Create the main parser
    main_parser = argparse.ArgumentParser(description="Main parser")
    subparsers = main_parser.add_subparsers(dest='subparser_name', help='sub-command help')

    # Example sub-parser 1
    parser_a = subparsers.add_parser('command_a', help='command_a help')
    parser_a.add_argument('--arg1', type=int, help='arg1 help')

    # Example sub-parser 2
    parser_b = subparsers.add_parser('command_b', help='command_b help')
    parser_b.add_argument('--arg2', type=str, help='arg2 help')

    # Parse the arguments
    args = main_parser.parse_args(list(unparsed_arguments))

    # Organize the parsed arguments into a dictionary
    parsed_args = {}
    if args.subparser_name:
        parsed_args[args.subparser_name] = args
    else:
        parsed_args['global'] = args

    return parsed_args