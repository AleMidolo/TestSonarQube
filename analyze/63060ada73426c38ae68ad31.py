def _convert_non_cli_args(self, parser_name, values_dict):
    """
    通过修改 values_dict 参数将参数转换为正确的类型。

    默认情况下，所有的值都是字符串。

    :param parser_name: 命令名称，例如 main、virsh、ospd 等
    :param values_dict: 包含参数的字典
    """
    if parser_name == 'main':
        # 假设 main 命令的参数需要转换为整数
        for key, value in values_dict.items():
            if key in ['port', 'timeout']:
                values_dict[key] = int(value)
    elif parser_name == 'virsh':
        # 假设 virsh 命令的参数需要转换为布尔值
        for key, value in values_dict.items():
            if key in ['verbose', 'debug']:
                values_dict[key] = value.lower() == 'true'
    elif parser_name == 'ospd':
        # 假设 ospd 命令的参数需要转换为浮点数
        for key, value in values_dict.items():
            if key in ['threshold', 'rate']:
                values_dict[key] = float(value)
    # 可以根据需要添加更多的 parser_name 处理逻辑
    return values_dict