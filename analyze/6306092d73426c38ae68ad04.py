def get_parser_option_specs(self, command_name):
    """
    获取指定命令的所有选项

    :param command_name: 命令名称（如 main、virsh、ospd 等）
    :return: 所有命令选项的列表
    """
    # 假设我们有一个字典存储命令及其选项
    command_options = {
        'main': ['--help', '--version', '--verbose'],
        'virsh': ['--connect', '--list', '--start'],
        'ospd': ['--config', '--debug', '--status']
    }
    
    # 返回指定命令的选项，如果命令不存在则返回空列表
    return command_options.get(command_name, [])