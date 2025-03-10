import argparse

def parse_arguments(*unparsed_arguments):
    """
    给定调用此脚本时提供的命令行参数，解析这些参数并返回一个字典。
    该字典将子解析器名称（或 "global"）映射到一个 argparse.Namespace 实例。
    """
    parser = argparse.ArgumentParser(description="Main parser")
    subparsers = parser.add_subparsers(dest='subparser_name', help='sub-command help')

    # Example subparser
    parser_a = subparsers.add_parser('command_a', help='command_a help')
    parser_a.add_argument('--arg1', type=int, help='arg1 help')

    parser_b = subparsers.add_parser('command_b', help='command_b help')
    parser_b.add_argument('--arg2', type=str, help='arg2 help')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    parsed_args = {}
    if hasattr(args, 'subparser_name'):
        parsed_args[args.subparser_name] = args
    else:
        parsed_args['global'] = args

    return parsed_args