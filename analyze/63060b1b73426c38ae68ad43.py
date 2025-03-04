def extend_cli(self, root_subparsers):
    """
    将规范 CLI 选项添加到主入口点。

    :param subparser: 要扩展的子解析器对象。
    """
    # 创建规范子命令解析器
    parser = root_subparsers.add_parser(
        'standard',
        help='Standard code formatting and linting options'
    )

    # 添加规范相关的命令行参数
    parser.add_argument(
        '--style',
        choices=['pep8', 'google', 'numpy'],
        default='pep8',
        help='Code style to enforce'
    )

    parser.add_argument(
        '--max-line-length',
        type=int,
        default=79,
        help='Maximum allowed line length'
    )

    parser.add_argument(
        '--ignore',
        nargs='+',
        default=[],
        help='List of error codes to ignore'
    )

    parser.add_argument(
        '--select',
        nargs='+', 
        default=[],
        help='List of error codes to specifically check'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Increase output verbosity'
    )

    # 设置函数来处理该子命令
    parser.set_defaults(func=self.handle_standard_command)