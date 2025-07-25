def extend_cli(self, root_subparsers):
    """
    将规范 CLI 选项添加到主入口点。

    :param subparser: 要扩展的子解析器对象。
    """
    # 示例代码：添加一个子命令
    parser = root_subparsers.add_parser('example', help='示例子命令')
    parser.add_argument('--option', type=str, help='示例选项')
    
    # 其他选项和参数可以在这里添加