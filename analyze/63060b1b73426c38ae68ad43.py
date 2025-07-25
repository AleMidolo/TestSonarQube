def extend_cli(self, root_subparsers):
    """
    将规范 CLI 选项添加到主入口点。

    :param subparser: 要扩展的子解析器对象。
    """
    # 创建一个新的子命令解析器
    parser = root_subparsers.add_parser(
        'standards',
        help='Standards and specifications related commands'
    )

    # 创建子命令的子解析器
    subparsers = parser.add_subparsers(
        title='Standards commands',
        dest='standards_command'
    )

    # 添加列出标准的命令
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

    # 添加查看标准详情的命令
    view_parser = subparsers.add_parser(
        'view',
        help='View standard details'
    )
    view_parser.add_argument(
        'standard_id',
        help='ID of the standard to view'
    )

    # 添加验证标准的命令
    validate_parser = subparsers.add_parser(
        'validate',
        help='Validate against a standard'
    )
    validate_parser.add_argument(
        'standard_id',
        help='ID of the standard to validate against'
    )
    validate_parser.add_argument(
        'input_file',
        help='File to validate'
    )

    return parser