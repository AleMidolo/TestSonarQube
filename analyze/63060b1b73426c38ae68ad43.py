def extend_cli(self, root_subparsers):
    """
    将规范 CLI 选项添加到主入口点。

    :param root_subparsers: 要扩展的子解析器对象。
    """
    # 添加一个子命令 '规范'
    parser = root_subparsers.add_parser('规范', help='规范相关操作')
    
    # 添加子命令 '生成'
    generate_parser = parser.add_subparsers(dest='generate_command', help='生成规范')
    generate_parser.add_parser('生成', help='生成规范文件')
    
    # 添加子命令 '验证'
    validate_parser = parser.add_subparsers(dest='validate_command', help='验证规范')
    validate_parser.add_parser('验证', help='验证规范文件')