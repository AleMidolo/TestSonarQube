import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script, analizza gli argomenti e restituiscili come un dizionario che mappa il nome del sotto-parser (o "global") a un'istanza di `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(description="Main parser")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-commands")

    # Example subparser
    subparser_example = subparsers.add_parser("example", help="Example sub-command")
    subparser_example.add_argument("--example_arg", type=str, help="Example argument")

    # Global arguments
    parser.add_argument("--global_arg", type=str, help="Global argument")

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    parsed_args = {}
    if hasattr(args, "subparser_name"):
        parsed_args[args.subparser_name] = args
    else:
        parsed_args["global"] = args

    return parsed_args