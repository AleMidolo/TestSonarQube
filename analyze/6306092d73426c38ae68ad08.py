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
            
        condition = option['required_when']
        
        # If condition is a string, treat it as a dependent argument
        if isinstance(condition, str):
            if args.get(condition):
                required_args.append(option['name'])
                
        # If condition is a dict, evaluate the condition
        elif isinstance(condition, dict):
            should_require = True
            
            for key, value in condition.items():
                if args.get(key) != value:
                    should_require = False
                    break
                    
            if should_require:
                required_args.append(option['name'])
                
        # If condition is a callable, call it with args
        elif callable(condition):
            if condition(args):
                required_args.append(option['name'])
                
    return required_args