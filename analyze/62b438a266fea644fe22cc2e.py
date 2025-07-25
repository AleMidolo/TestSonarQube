import argparse

def parse_arguments(*unparsed_arguments):
    """
    给定调用此脚本时提供的命令行参数，解析这些参数并返回一个字典。
    该字典将子解析器名称（或 "global"）映射到一个 argparse.Namespace 实例。
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    subparsers = parser.add_subparsers(dest='subparser_name', help='Sub-command help')

    # Example subparser
    parser_a = subparsers.add_parser('command_a', help='Command A help')
    parser_a.add_argument('--arg1', type=int, help='Argument 1 for command A')

    # Another example subparser
    parser_b = subparsers.add_parser('command_b', help='Command B help')
    parser_b.add_argument('--arg2', type=str, help='Argument 2 for command B')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    parsed_args = {}
    if hasattr(args, 'subparser_name'):
        parsed_args[args.subparser_name] = args
    else:
        parsed_args['global'] = args

    return parsed_args