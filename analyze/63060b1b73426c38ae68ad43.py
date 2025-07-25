def extend_cli(self, root_subparsers):
    """
    将规范 CLI 选项添加到主入口点。

    :param root_subparsers: 要扩展的子解析器对象。
    """
    # 添加一个子命令
    subparser = root_subparsers.add_parser('extend', help='扩展 CLI 选项')
    
    # 添加一个选项
    subparser.add_argument('--option', type=str, help='示例选项')
    
    # 添加另一个选项
    subparser.add_argument('--flag', action='store_true', help='示例标志')