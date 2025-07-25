import argparse

def parse_arguments(*unparsed_arguments):
    """
    解析参数并将其作为字典映射返回

    给定调用该脚本时使用的命令行参数，解析这些参数并返回一个字典，该字典将子解析器名称（或 "global"）映射到相应的 argparse.Namespace 实例。
    """
    parser = argparse.ArgumentParser(description="Global parser")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser
    subparser1 = subparsers.add_parser('subcommand1', help='Subcommand 1 help')
    subparser1.add_argument('--arg1', type=str, help='Argument 1 for subcommand1')

    subparser2 = subparsers.add_parser('subcommand2', help='Subcommand 2 help')
    subparser2.add_argument('--arg2', type=int, help='Argument 2 for subcommand2')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to map subparser names to their respective Namespace objects
    result = {}
    if hasattr(args, 'subparser_name'):
        result[args.subparser_name] = args
    else:
        result['global'] = args

    return result