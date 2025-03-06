def get_parser_option_specs(self, command_name):
    """
    获取指定命令的所有选项

    :param command_name: 命令名称（如 main、virsh、ospd 等）
    :return: 所有命令选项的列表
    """
    # 假设 self.parsers 是一个字典，存储了不同命令的解析器
    if command_name in self.parsers:
        parser = self.parsers[command_name]
        # 获取解析器中的所有选项
        options = []
        for action in parser._actions:
            if action.option_strings:
                options.append({
                    'option_strings': action.option_strings,
                    'help': action.help,
                    'dest': action.dest,
                    'required': action.required,
                    'default': action.default
                })
        return options
    else:
        return []