def parse_arguments(*unparsed_arguments):
    """
    解析参数并将其作为字典映射返回

    给定调用该脚本时使用的命令行参数，解析这些参数并返回一个字典，该字典将子解析器名称（或 "global"）映射到相应的 argparse.Namespace 实例。
    """
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Example subparser
    subparser_a = subparsers.add_parser('sub_a')
    subparser_a.add_argument('--option_a', type=str, help='Option for subparser A')

    subparser_b = subparsers.add_parser('sub_b')
    subparser_b.add_argument('--option_b', type=int, help='Option for subparser B')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to hold the results
    result = {}
    if args.subparser_name:
        result[args.subparser_name] = args
    else:
        result['global'] = args

    return result