def _convert_non_cli_args(self, parser_name, values_dict):
    """
    通过修改 values_dict 参数将参数转换为正确的类型。

    默认情况下，所有的值都是字符串。

    :param parser_name: 命令名称，例如 main、virsh、ospd 等
    :param values_dict: 包含参数的字典
    """
    if parser_name == 'main':
        for key, value in values_dict.items():
            if value.isdigit():
                values_dict[key] = int(value)
            elif value.replace('.', '', 1).isdigit():
                values_dict[key] = float(value)
            elif value.lower() in ('true', 'false'):
                values_dict[key] = value.lower() == 'true'
    elif parser_name == 'virsh':
        for key, value in values_dict.items():
            if key in ['memory', 'vcpu']:
                values_dict[key] = int(value)
            elif key in ['autostart', 'persistent']:
                values_dict[key] = value.lower() == 'true'
    elif parser_name == 'ospd':
        for key, value in values_dict.items():
            if key in ['port', 'timeout']:
                values_dict[key] = int(value)
            elif key in ['verbose', 'debug']:
                values_dict[key] = value.lower() == 'true'
    # 可以根据需要添加更多的 parser_name 处理逻辑
    return values_dict