def extend_cli(self, root_subparsers):
    """
    将规范 CLI 选项添加到主入口点。

    :param subparser: 要扩展的子解析器对象。
    """
    # 假设我们要添加一个名为 'example' 的子命令
    example_parser = root_subparsers.add_parser('example', help='示例命令的帮助信息')
    
    # 添加选项
    example_parser.add_argument('--option', type=str, help='示例选项')
    
    # 处理其他选项和参数
    # ...