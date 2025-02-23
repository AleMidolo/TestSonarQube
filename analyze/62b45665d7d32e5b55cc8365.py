def parse_arguments(*unparsed_arguments):
    """
    解析参数并将其作为字典映射返回

    给定调用该脚本时使用的命令行参数，解析这些参数并返回一个字典，该字典将子解析器名称（或 "global"）映射到相应的 argparse.Namespace 实例。
    """
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Example subparser for 'command1'
    command1_parser = subparsers.add_parser('command1')
    command1_parser.add_argument('--option1', type=str, help='Option for command1')

    # Example subparser for 'command2'
    command2_parser = subparsers.add_parser('command2')
    command2_parser.add_argument('--option2', type=int, help='Option for command2')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Return as a dictionary mapping subparser names to their respective Namespace
    return {args.subparser_name: args} if args.subparser_name else {'global': args}