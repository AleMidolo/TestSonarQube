import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dato un insieme di argomenti della riga di comando con cui è stato invocato questo script, analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser (o "global") a un'istanza di argparse.Namespace.
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Esempio di sotto-parser
    parser_a = subparsers.add_parser('command_a')
    parser_a.add_argument('--option_a', type=str, help='Opzione per il comando A')

    parser_b = subparsers.add_parser('command_b')
    parser_b.add_argument('--option_b', type=int, help='Opzione per il comando B')

    # Analizza gli argomenti
    args = parser.parse_args(unparsed_arguments)

    # Restituisce un dizionario con il nome del sotto-parser e l'istanza di Namespace
    return {args.subparser_name: args}