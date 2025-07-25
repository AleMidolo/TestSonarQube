def get_option_spec(self, command_name, argument_name):
    """
    获取指定选项名称的规范。通过 `self.get_parser_option_specs()` 获取给定 `command_name` 的选项。
    获取指定选项名称的规范。

    Args:
        command_name (str): 命令名称。
        argument_name (str): 参数名称。

    Returns:
        dict: 指定选项的规范。
    """
    option_specs = self.get_parser_option_specs(command_name)
    return option_specs.get(argument_name, {})