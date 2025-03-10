def get_parser_option_specs(self, command_name):
    """
    获取指定命令的所有选项

    :param command_name: 命令名称（如 main、virsh、ospd 等）
    :return: 所有命令选项的列表
    """
    # 假设 self.parser 是一个 argparse.ArgumentParser 对象
    if command_name in self.parser._actions:
        return [action.option_strings for action in self.parser._actions if action.option_strings]
    else:
        return []