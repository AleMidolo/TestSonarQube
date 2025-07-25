import argparse

def parse_arguments(*unparsed_arguments):
    """
    给定调用此脚本时提供的命令行参数，解析这些参数并返回一个字典。
    该字典将子解析器名称（或 "global"）映射到一个 argparse.Namespace 实例。
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Add global arguments
    parser.add_argument('--global-arg', type=str, help='A global argument.')
    
    # Create subparsers
    subparsers = parser.add_subparsers(dest='subparser_name', help='Sub-command help')
    
    # Subparser for command 'foo'
    parser_foo = subparsers.add_parser('foo', help='foo help')
    parser_foo.add_argument('--foo-arg', type=int, help='foo argument')
    
    # Subparser for command 'bar'
    parser_bar = subparsers.add_parser('bar', help='bar help')
    parser_bar.add_argument('--bar-arg', type=float, help='bar argument')
    
    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)
    
    # Organize the parsed arguments into a dictionary
    parsed_args = {}
    if hasattr(args, 'subparser_name'):
        parsed_args[args.subparser_name] = args
    else:
        parsed_args['global'] = args
    
    return parsed_args