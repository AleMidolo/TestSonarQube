import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dado un conjunto de argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como un diccionario que mapea desde el nombre del subparser (o "global") a una instancia de `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Global arguments
    parser.add_argument("--global-arg", type=str, help="A global argument")

    # Subparser 1
    parser_sub1 = subparsers.add_parser("sub1", help="Subparser 1 help")
    parser_sub1.add_argument("--sub1-arg", type=str, help="Subparser 1 argument")

    # Subparser 2
    parser_sub2 = subparsers.add_parser("sub2", help="Subparser 2 help")
    parser_sub2.add_argument("--sub2-arg", type=int, help="Subparser 2 argument")

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Organize the arguments into a dictionary
    parsed_args = {}
    if hasattr(args, "subparser_name"):
        parsed_args[args.subparser_name] = args
    else:
        parsed_args["global"] = args

    return parsed_args