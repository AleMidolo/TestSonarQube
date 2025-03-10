import argparse

def parse_arguments(*unparsed_arguments):
    """
    给定调用此脚本时提供的命令行参数，解析这些参数并返回一个字典。
    该字典将子解析器名称（或 "global"）映射到一个 argparse.Namespace 实例。
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # 添加全局参数
    parser.add_argument('--global-arg', type=str, help='A global argument')
    
    # 创建子解析器
    subparsers = parser.add_subparsers(dest='subparser_name', help='Sub-command help')
    
    # 子解析器1
    parser_sub1 = subparsers.add_parser('sub1', help='Subparser 1 help')
    parser_sub1.add_argument('--sub1-arg', type=str, help='Subparser 1 argument')
    
    # 子解析器2
    parser_sub2 = subparsers.add_parser('sub2', help='Subparser 2 help')
    parser_sub2.add_argument('--sub2-arg', type=int, help='Subparser 2 argument')
    
    # 解析参数
    args = parser.parse_args(unparsed_arguments)
    
    # 将结果组织成字典
    result = {}
    if args.subparser_name:
        result[args.subparser_name] = args
    else:
        result['global'] = args
    
    return result