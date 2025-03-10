import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dato un insieme di argomenti della riga di comando con cui è stato invocato questo script,
    analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser
    (o "global") a un'istanza di argparse.Namespace.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Global arguments
    parser.add_argument("--global-arg", type=str, help="Global argument")

    # Sub-parser 1
    parser_sub1 = subparsers.add_parser("sub1", help="Sub-parser 1 help")
    parser_sub1.add_argument("--sub1-arg", type=str, help="Sub-parser 1 argument")

    # Sub-parser 2
    parser_sub2 = subparsers.add_parser("sub2", help="Sub-parser 2 help")
    parser_sub2.add_argument("--sub2-arg", type=int, help="Sub-parser 2 argument")

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    parsed_args = {}
    if args.subparser_name:
        parsed_args[args.subparser_name] = args
    else:
        parsed_args["global"] = args

    return parsed_args