def _convert_non_cli_args(self, parser_name, values_dict):
    """
    通过修改 values_dict 参数将参数转换为正确的类型。

    默认情况下，所有的值都是字符串。

    :param parser_name: 命令名称，例如 main、virsh、ospd 等
    :param values_dict: 包含参数的字典
    """
    for key, value in values_dict.items():
        if isinstance(value, str):
            # 尝试将字符串转换为整数
            if value.isdigit():
                values_dict[key] = int(value)
            # 尝试将字符串转换为浮点数
            elif value.replace('.', '', 1).isdigit():
                values_dict[key] = float(value)
            # 尝试将字符串转换为布尔值
            elif value.lower() in ('true', 'false'):
                values_dict[key] = value.lower() == 'true'
            # 其他情况保持为字符串
            else:
                values_dict[key] = value
    return values_dict