import argparse

def make_parsers():
    """
    构建一个解析器及其子解析器，并将它们作为一个元组返回。

    构建一个顶级解析器及其子解析器，并将它们作为一个元组返回。
    """
    # 创建顶级解析器
    parser = argparse.ArgumentParser(description="顶级解析器")
    
    # 创建子解析器
    subparsers = parser.add_subparsers(dest="command", help="子命令")
    
    # 添加子命令1
    parser_a = subparsers.add_parser('command_a', help='子命令A的帮助信息')
    parser_a.add_argument('--arg1', type=int, help='子命令A的参数1')
    
    # 添加子命令2
    parser_b = subparsers.add_parser('command_b', help='子命令B的帮助信息')
    parser_b.add_argument('--arg2', type=str, help='子命令B的参数2')
    
    return parser, subparsers