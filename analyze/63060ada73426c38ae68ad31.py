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
    parser = self._parsers.get(parser_name)
    if not parser:
        return

    # 遍历所有参数
    for arg_name, value in values_dict.items():
        # 跳过None值
        if value is None:
            continue
            
        # 获取参数的类型
        arg_type = None
        for action in parser._actions:
            if action.dest == arg_name:
                arg_type = action.type
                break
                
        # 如果找到类型定义则进行转换
        if arg_type:
            try:
                # 处理列表类型
                if isinstance(value, list):
                    values_dict[arg_name] = [arg_type(v) for v in value]
                else:
                    values_dict[arg_name] = arg_type(value)
            except (ValueError, TypeError):
                # 转换失败时保持原值
                continue