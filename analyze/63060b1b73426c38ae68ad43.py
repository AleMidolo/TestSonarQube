def extend_cli(self, root_subparsers):
    """
    将规范 CLI 选项添加到主入口点。

    :param root_subparsers: 要扩展的子解析器对象。
    """
    # 添加一个子命令 '规范'
    parser = root_subparsers.add_parser('规范', help='规范相关操作')
    
    # 添加子命令 '规范' 的子命令
    subparsers = parser.add_subparsers(dest='规范操作', help='规范操作')

    # 添加子命令 '添加'
    add_parser = subparsers.add_parser('添加', help='添加规范')
    add_parser.add_argument('名称', type=str, help='规范名称')
    add_parser.add_argument('描述', type=str, help='规范描述')

    # 添加子命令 '删除'
    delete_parser = subparsers.add_parser('删除', help='删除规范')
    delete_parser.add_argument('名称', type=str, help='规范名称')

    # 添加子命令 '列表'
    list_parser = subparsers.add_parser('列表', help='列出所有规范')