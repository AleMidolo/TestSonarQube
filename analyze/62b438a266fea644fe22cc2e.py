import argparse

def parse_arguments(*unparsed_arguments):
    """
    给定调用此脚本时提供的命令行参数，解析这些参数并返回一个字典。
    该字典将子解析器名称（或 "global"）映射到一个 argparse.Namespace 实例。
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser for 'command1'
    parser_command1 = subparsers.add_parser('command1', help='Command1 help')
    parser_command1.add_argument('--arg1', type=str, help='Argument 1 for command1')

    # Example subparser for 'command2'
    parser_command2 = subparsers.add_parser('command2', help='Command2 help')
    parser_command2.add_argument('--arg2', type=int, help='Argument 2 for command2')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to map subparser names to their respective Namespace objects
    parsed_arguments = {}
    if hasattr(args, 'subparser_name'):
        parsed_arguments[args.subparser_name] = args
    else:
        parsed_arguments['global'] = args

    return parsed_arguments