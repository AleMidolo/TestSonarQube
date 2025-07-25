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
        # Skip if option has no required_when condition
        if 'required_when' not in option:
            continue
            
        required_when = option['required_when']
        
        # If required_when is a string (argument name)
        if isinstance(required_when, str):
            if args.get(required_when):
                required_args.append(option['name'])
                
        # If required_when is a dict with conditions
        elif isinstance(required_when, dict):
            conditions_met = True
            for key, value in required_when.items():
                if args.get(key) != value:
                    conditions_met = False
                    break
            
            if conditions_met:
                required_args.append(option['name'])
                
        # If required_when is a callable
        elif callable(required_when):
            if required_when(args):
                required_args.append(option['name'])
                
    return required_args