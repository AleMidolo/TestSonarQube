def _convert_non_cli_args(self, parser_name, values_dict):
    """
    通过修改 values_dict 参数将参数转换为正确的类型。

    默认情况下，所有的值都是字符串。

    :param parser_name: 命令名称，例如 main、virsh、ospd 等
    :param values_dict: 包含参数的字典
    """
    if not values_dict:
        return

    # 获取该解析器的参数定义
    parser_args = self.get_parser_args(parser_name)
    if not parser_args:
        return

    # 遍历字典中的每个参数
    for arg_name, value in values_dict.items():
        # 跳过None值
        if value is None:
            continue
            
        # 获取参数定义
        arg_def = parser_args.get(arg_name)
        if not arg_def:
            continue

        # 获取参数类型
        arg_type = arg_def.get('type')
        if not arg_type:
            continue

        try:
            # 根据定义的类型转换值
            if arg_type == bool:
                if isinstance(value, str):
                    values_dict[arg_name] = value.lower() in ('true', 'yes', '1', 'on')
            elif arg_type == int:
                values_dict[arg_name] = int(value)
            elif arg_type == float:
                values_dict[arg_name] = float(value)
            elif arg_type == list:
                if isinstance(value, str):
                    values_dict[arg_name] = value.split(',')
        except (ValueError, TypeError):
            # 如果转换失败，保持原值不变
            continue