import argparse

def make_parsers():
    """
    创建一个顶级解析器及其子解析器，并将它们作为元组返回。
    """
    # 创建顶级解析器
    parser = argparse.ArgumentParser(description="顶级解析器")
    
    # 创建子解析器
    subparsers = parser.add_subparsers(dest="command", help="子命令")
    
    # 添加第一个子命令
    parser_a = subparsers.add_parser('command_a', help='命令A的帮助信息')
    parser_a.add_argument('--arg1', type=int, help='参数1的帮助信息')
    
    # 添加第二个子命令
    parser_b = subparsers.add_parser('command_b', help='命令B的帮助信息')
    parser_b.add_argument('--arg2', type=str, help='参数2的帮助信息')
    
    return parser, subparsers