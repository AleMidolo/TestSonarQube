def _convert_non_cli_args(self, parser_name, values_dict):
    """
    通过修改 values_dict 参数将参数转换为正确的类型。

    默认情况下，所有的值都是字符串。

    :param parser_name: 命令名称，例如 main、virsh、ospd 等
    :param values_dict: 包含参数的字典
    """
    for key, value in values_dict.items():
        if value.isdigit():
            values_dict[key] = int(value)
        else:
            try:
                # Attempt to convert to float if it's not an integer
                values_dict[key] = float(value)
            except ValueError:
                # Keep it as a string if it can't be converted
                values_dict[key] = value