def _convert_non_cli_args(self, parser_name, values_dict):
    """
    通过修改 values_dict 参数将参数转换为正确的类型。

    默认情况下，所有的值都是字符串。

    :param parser_name: 命令名称，例如 main、virsh、ospd 等
    :param values_dict: 包含参数的字典
    """
    if parser_name == "main":
        # 根据 main 命令的特定需求进行类型转换
        for key, value in values_dict.items():
            if key == "port":
                values_dict[key] = int(value)
            elif key == "verbose":
                values_dict[key] = bool(value)
            elif key == "timeout":
                values_dict[key] = float(value)
    elif parser_name == "virsh":
        # 根据 virsh 命令的特定需求进行类型转换
        for key, value in values_dict.items():
            if key == "memory":
                values_dict[key] = int(value)
            elif key == "cpu":
                values_dict[key] = int(value)
    elif parser_name == "ospd":
        # 根据 ospd 命令的特定需求进行类型转换
        for key, value in values_dict.items():
            if key == "threads":
                values_dict[key] = int(value)
            elif key == "debug":
                values_dict[key] = bool(value)
    else:
        # 默认情况下，尝试将值转换为整数或浮点数
        for key, value in values_dict.items():
            try:
                values_dict[key] = int(value)
            except ValueError:
                try:
                    values_dict[key] = float(value)
                except ValueError:
                    pass