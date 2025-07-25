import argparse

def parse_arguments(*unparsed_arguments):
    """
    给定调用此脚本时提供的命令行参数，解析这些参数并返回一个字典。
    该字典将子解析器名称（或 "global"）映射到一个 argparse.Namespace 实例。
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Example subparser
    subparser_a = subparsers.add_parser('sub_a')
    subparser_a.add_argument('--option_a', type=str, help='Option for subparser A')

    subparser_b = subparsers.add_parser('sub_b')
    subparser_b.add_argument('--option_b', type=int, help='Option for subparser B')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Return a dictionary mapping subparser names to their respective Namespace
    return {args.subparser_name if args.subparser_name else 'global': args}