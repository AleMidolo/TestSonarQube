import argparse

def parse_arguments(*unparsed_arguments):
    """
    解析参数并将其作为字典映射返回

    给定调用该脚本时使用的命令行参数，解析这些参数并返回一个字典，该字典将子解析器名称（或 "global"）映射到相应的 argparse.Namespace 实例。
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Example subparser for 'command1'
    parser_command1 = subparsers.add_parser('command1', help='Command1 help')
    parser_command1.add_argument('--arg1', type=int, help='Argument 1 for command1')

    # Example subparser for 'command2'
    parser_command2 = subparsers.add_parser('command2', help='Command2 help')
    parser_command2.add_argument('--arg2', type=str, help='Argument 2 for command2')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to map the command to its arguments
    result = {}
    if hasattr(args, 'command'):
        result[args.command] = args
    else:
        result['global'] = args

    return result