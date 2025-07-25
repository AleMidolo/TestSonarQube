def extend_cli(self, root_subparsers):
    """
    将规范 CLI 选项添加到主入口点。

    :param subparser: 要扩展的子解析器对象。
    """
    # 创建一个新的子解析器
    parser = root_subparsers.add_parser(
        'standards',
        help='Standards and specifications related commands'
    )

    # 添加子命令解析器
    subparsers = parser.add_subparsers(
        title='Standards commands',
        dest='standards_command'
    )

    # 添加列表命令
    list_parser = subparsers.add_parser(
        'list',
        help='List available standards'
    )
    list_parser.add_argument(
        '--format',
        choices=['text', 'json'],
        default='text',
        help='Output format'
    )

    # 添加验证命令
    validate_parser = subparsers.add_parser(
        'validate',
        help='Validate against standards'
    )
    validate_parser.add_argument(
        'standard',
        help='Standard to validate against'
    )
    validate_parser.add_argument(
        'file',
        help='File to validate'
    )

    # 添加信息命令
    info_parser = subparsers.add_parser(
        'info',
        help='Show detailed information about a standard'
    )
    info_parser.add_argument(
        'standard',
        help='Standard to show information about'
    )