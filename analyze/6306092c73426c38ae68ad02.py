def validate_arg_deprecation(self, cli_args, answer_file_args):
    deprecated_args = set(cli_args.keys()).intersection(set(answer_file_args.keys()))
    if deprecated_args:
        print("Deprecated arguments detected:")
        for arg in deprecated_args:
            print(f" - {arg}")
    else:
        print("No deprecated arguments found.")