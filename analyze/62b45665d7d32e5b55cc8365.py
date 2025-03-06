import argparse

def parse_arguments(*unparsed_arguments):
    """
    解析参数并将其作为字典映射返回

    给定调用该脚本时使用的命令行参数，解析这些参数并返回一个字典，该字典将子解析器名称（或 "global"）映射到相应的 argparse.Namespace 实例。
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    subparsers = parser.add_subparsers(dest='subparser_name', help='sub-command help')

    # Example subparser for 'command1'
    parser_command1 = subparsers.add_parser('command1', help='command1 help')
    parser_command1.add_argument('--arg1', type=str, help='arg1 help')

    # Example subparser for 'command2'
    parser_command2 = subparsers.add_parser('command2', help='command2 help')
    parser_command2.add_argument('--arg2', type=int, help='arg2 help')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to map subparser names to their respective Namespace objects
    parsed_arguments = {}
    if hasattr(args, 'subparser_name'):
        parsed_arguments[args.subparser_name] = args
    else:
        parsed_arguments['global'] = args

    return parsed_arguments