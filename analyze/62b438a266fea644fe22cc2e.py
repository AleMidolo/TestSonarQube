import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y devuélvelos como un diccionario que mapea desde el nombre del subparser (o "global") a una instancia de `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser
    subparser_example = subparsers.add_parser("example", help="Example subparser")
    subparser_example.add_argument("--example_arg", type=str, help="Example argument")

    # Parse the arguments
    parsed_args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to map subparser names to their parsed arguments
    args_dict = {}
    if parsed_args.subparser_name:
        args_dict[parsed_args.subparser_name] = parsed_args
    else:
        args_dict["global"] = parsed_args

    return args_dict