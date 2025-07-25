def _get_conditionally_required_args(self, command_name, options_spec, args):
    """
    列出符合 ``required_when`` 条件的参数。

    :param command_name: 命令名称。
    :param options_spec: 命令选项规范的列表。
    :param args: 接收到的输入参数。
    :return: list，符合 ``required_when`` 条件的参数名称列表。
    """
    required_args = []
    
    for option in options_spec:
        if 'required_when' in option:
            condition = option['required_when']
            if condition['command'] == command_name:
                if condition['condition'](args):
                    required_args.append(option['name'])
    
    return required_args