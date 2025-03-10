import argparse

def make_parsers():
    """
    创建一个顶级解析器及其子解析器，并将它们作为元组返回。
    """
    # 创建顶级解析器
    parser = argparse.ArgumentParser(description="顶级解析器")
    
    # 创建子解析器
    subparsers = parser.add_subparsers(title="子命令", dest="subcommand")
    
    # 添加第一个子解析器
    parser_a = subparsers.add_parser("command_a", help="执行命令A")
    parser_a.add_argument("--option_a", type=int, help="命令A的选项")
    
    # 添加第二个子解析器
    parser_b = subparsers.add_parser("command_b", help="执行命令B")
    parser_b.add_argument("--option_b", type=str, help="命令B的选项")
    
    return parser, subparsers