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
        # 检查选项是否有required_when条件
        if 'required_when' in option:
            condition = option['required_when']
            
            # 如果条件是字符串,视为依赖其他参数
            if isinstance(condition, str):
                # 检查依赖的参数是否存在且有值
                if condition in args and args[condition]:
                    required_args.append(option['name'])
                    
            # 如果条件是函数,执行函数检查
            elif callable(condition):
                if condition(args):
                    required_args.append(option['name'])
                    
            # 如果条件是字典,检查多个参数条件
            elif isinstance(condition, dict):
                matches = True
                for key, value in condition.items():
                    if key not in args or args[key] != value:
                        matches = False
                        break
                if matches:
                    required_args.append(option['name'])
    
    return required_args