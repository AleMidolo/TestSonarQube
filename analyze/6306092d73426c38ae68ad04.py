def get_parser_option_specs(self, command_name):
    """
    获取指定命令的所有选项

    :param command_name: 命令名称（如 main、virsh、ospd 等）
    :return: 所有命令选项的列表
    """
    if not hasattr(self, '_parser_options'):
        self._parser_options = {}
    
    if command_name not in self._parser_options:
        self._parser_options[command_name] = []
    
    return self._parser_options[command_name]