import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script, analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser (o "global") a un'istanza di `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Example of adding subparsers
    subparser_a = subparsers.add_parser('sub_a')
    subparser_a.add_argument('--option_a', type=str, help='Option for subparser A')

    subparser_b = subparsers.add_parser('sub_b')
    subparser_b.add_argument('--option_b', type=int, help='Option for subparser B')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Return as a dictionary mapping subparser name to Namespace
    return {args.subparser_name: args}