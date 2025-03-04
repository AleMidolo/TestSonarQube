def extend_cli(self, root_subparsers):
    """
    将规范 CLI 选项添加到主入口点。

    :param subparser: 要扩展的子解析器对象。
    """
    # 创建子命令解析器
    parser = root_subparsers.add_parser(
        'standards',
        help='Standards and specifications related commands'
    )
    
    # 添加子命令
    subparsers = parser.add_subparsers(
        title='Standards commands',
        dest='standards_command'
    )
    
    # 添加列表命令
    list_parser = subparsers.add_parser(
        'list',
        help='List available standards'
    )
    
    # 添加查看命令
    view_parser = subparsers.add_parser(
        'view',
        help='View details of a specific standard'
    )
    view_parser.add_argument(
        'standard_id',
        help='ID of the standard to view'
    )
    
    # 添加验证命令
    validate_parser = subparsers.add_parser(
        'validate',
        help='Validate against a standard'
    )
    validate_parser.add_argument(
        'standard_id',
        help='ID of the standard to validate against'
    )
    validate_parser.add_argument(
        'target',
        help='Target to validate'
    )