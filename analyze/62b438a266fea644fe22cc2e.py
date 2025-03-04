def parse_arguments(*unparsed_arguments):
    """
    Dato un insieme di argomenti della riga di comando con cui è stato invocato questo script, analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser (o "global") a un'istanza di argparse.Namespace.
    """
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Example of adding subparsers
    subparser_a = subparsers.add_parser('command_a')
    subparser_a.add_argument('--option_a', type=str, help='Option for command_a')

    subparser_b = subparsers.add_parser('command_b')
    subparser_b.add_argument('--option_b', type=int, help='Option for command_b')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Return as a dictionary mapping subparser name to Namespace
    return {args.subparser_name: args}