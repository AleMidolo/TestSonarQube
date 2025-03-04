def make_parsers():
    """
    构建一个解析器及其子解析器，并将它们作为一个元组返回。

    构建一个顶级解析器及其子解析器，并将它们作为一个元组返回。
    """
    import argparse
    
    # 创建顶级解析器
    parser = argparse.ArgumentParser(description='命令行工具')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # 创建子解析器
    parser_a = subparsers.add_parser('a', help='命令 a')
    parser_a.add_argument('--foo', type=str, help='foo 参数')
    
    parser_b = subparsers.add_parser('b', help='命令 b') 
    parser_b.add_argument('--bar', type=int, help='bar 参数')
    
    parser_c = subparsers.add_parser('c', help='命令 c')
    parser_c.add_argument('--baz', type=float, help='baz 参数')

    return parser, subparsers