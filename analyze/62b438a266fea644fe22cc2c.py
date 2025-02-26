import argparse

def make_parsers():
    """
    创建一个顶级解析器及其子解析器，并将它们作为元组返回。
    """
    top_parser = argparse.ArgumentParser(prog='TopParser')
    subparsers = top_parser.add_subparsers(dest='command')

    # 创建子解析器
    sub_parser_a = subparsers.add_parser('command_a', help='帮助信息 A')
    sub_parser_b = subparsers.add_parser('command_b', help='帮助信息 B')

    return top_parser, subparsers