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
    # 添加 add 子命令
    add_parser = subparsers.add_parser('add', help='添加操作')
    add_parser.add_argument('x', type=int, help='第一个数')
    add_parser.add_argument('y', type=int, help='第二个数')
    
    # 添加 list 子命令
    list_parser = subparsers.add_parser('list', help='列表操作')
    list_parser.add_argument('--all', action='store_true', help='显示所有内容')
    
    # 添加 delete 子命令
    delete_parser = subparsers.add_parser('delete', help='删除操作')
    delete_parser.add_argument('id', type=int, help='要删除的ID')
    
    return parser, subparsers