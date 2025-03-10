def extend_cli(self, root_subparsers):
    """
    将规范 CLI 选项添加到主入口点。

    :param root_subparsers: 要扩展的子解析器对象。
    """
    # 添加一个子命令
    subparser = root_subparsers.add_parser('extend', help='扩展命令的帮助信息')
    
    # 添加一个选项
    subparser.add_argument('--option', type=str, help='这是一个示例选项')
    
    # 添加一个标志
    subparser.add_argument('--flag', action='store_true', help='这是一个示例标志')