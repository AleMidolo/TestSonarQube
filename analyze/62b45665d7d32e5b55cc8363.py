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
    # 示例子命令1
    parser_a = subparsers.add_parser('command-a', help='命令A的帮助信息')
    parser_a.add_argument('--arg1', help='参数1的帮助信息')
    
    # 示例子命令2 
    parser_b = subparsers.add_parser('command-b', help='命令B的帮助信息')
    parser_b.add_argument('--arg2', help='参数2的帮助信息')
    
    return parser, subparsers