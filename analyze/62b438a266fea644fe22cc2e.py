import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y devuélvelos como un diccionario que mapea desde el nombre del subparser (o "global") a una instancia de `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser
    subparser_example = subparsers.add_parser("example", help="Example subcommand")
    subparser_example.add_argument("--example_arg", type=str, help="Example argument")

    # Global arguments
    parser.add_argument("--global_arg", type=str, help="Global argument")

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Organize arguments into a dictionary
    parsed_args = {}
    if args.subparser_name:
        parsed_args[args.subparser_name] = args
    else:
        parsed_args["global"] = args

    return parsed_args