import argparse

def parse_arguments(*unparsed_arguments):
    """
    解析参数并将其作为字典映射返回

    给定调用该脚本时使用的命令行参数，解析这些参数并返回一个字典，该字典将子解析器名称（或 "global"）映射到相应的 argparse.Namespace 实例。
    """
    parser = argparse.ArgumentParser(description="Global parser")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-commands")

    # Example subparser
    subparser1 = subparsers.add_parser('subcommand1', help='First subcommand')
    subparser1.add_argument('--arg1', type=str, help='Argument for subcommand1')

    subparser2 = subparsers.add_parser('subcommand2', help='Second subcommand')
    subparser2.add_argument('--arg2', type=int, help='Argument for subcommand2')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    parsed_args = {}
    if hasattr(args, 'subparser_name'):
        parsed_args[args.subparser_name] = args
    else:
        parsed_args['global'] = args

    return parsed_args