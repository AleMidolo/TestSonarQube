import argparse

def parse_arguments(*unparsed_arguments):
    """
    解析参数并将其作为字典映射返回

    给定调用该脚本时使用的命令行参数，解析这些参数并返回一个字典，该字典将子解析器名称（或 "global"）映射到相应的 argparse.Namespace 实例。
    """
    parser = argparse.ArgumentParser(description="Global parser")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser
    parser_a = subparsers.add_parser('command_a', help='Command A help')
    parser_a.add_argument('--arg1', type=int, help='Argument 1 for command A')

    parser_b = subparsers.add_parser('command_b', help='Command B help')
    parser_b.add_argument('--arg2', type=str, help='Argument 2 for command B')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to map subparser names to their respective Namespace objects
    result = {}
    if hasattr(args, 'subparser_name'):
        result[args.subparser_name] = args
    else:
        result['global'] = args

    return result