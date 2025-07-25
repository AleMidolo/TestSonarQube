def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Validates and prints the deprecated arguments.

    :param cli_args: the dict of arguments from cli
    :param answer_file_args:  the dict of arguments from files
    """
    deprecated_args = set(cli_args.keys()).intersection(answer_file_args.keys())
    
    if deprecated_args:
        print("Deprecated arguments found:")
        for arg in deprecated_args:
            print(f"- {arg} is deprecated and should not be used.")
    else:
        print("No deprecated arguments found.")