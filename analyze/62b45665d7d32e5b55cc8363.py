import argparse

def make_parsers():
    """
    构建一个解析器及其子解析器，并将它们作为一个元组返回。

    构建一个顶级解析器及其子解析器，并将它们作为一个元组返回。
    """
    # 创建顶级解析器
    top_parser = argparse.ArgumentParser(prog='top_parser')
    
    # 创建子解析器
    subparsers = top_parser.add_subparsers(dest='command', required=True)
    
    # 添加子解析器
    sub_parser_a = subparsers.add_parser('command_a', help='Help for command A')
    sub_parser_a.add_argument('--option_a', type=str, help='Option for command A')
    
    sub_parser_b = subparsers.add_parser('command_b', help='Help for command B')
    sub_parser_b.add_argument('--option_b', type=int, help='Option for command B')
    
    return top_parser, subparsers