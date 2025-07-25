import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script, analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser (o "global") a un'istanza di `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Example subparser for 'command1'
    command1_parser = subparsers.add_parser('command1')
    command1_parser.add_argument('--option1', type=str, help='Option for command1')

    # Example subparser for 'command2'
    command2_parser = subparsers.add_parser('command2')
    command2_parser.add_argument('--option2', type=int, help='Option for command2')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Return the parsed arguments as a dictionary
    return {args.subparser_name: args}