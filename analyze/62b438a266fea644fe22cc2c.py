import argparse

def make_parsers():
    """
    创建一个顶级解析器及其子解析器，并将它们作为元组返回。
    """
    top_parser = argparse.ArgumentParser(prog='Top Level Parser')
    subparsers = top_parser.add_subparsers(dest='command')

    # 创建子解析器
    sub_parser_a = subparsers.add_parser('command_a', help='帮助信息 A')
    sub_parser_a.add_argument('--option_a', type=str, help='选项 A')

    sub_parser_b = subparsers.add_parser('command_b', help='帮助信息 B')
    sub_parser_b.add_argument('--option_b', type=int, help='选项 B')

    return top_parser, subparsers