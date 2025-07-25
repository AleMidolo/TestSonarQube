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
        
        # If condition is a string, evaluate it as a Python expression
        if isinstance(condition, str):
            # Create a context with the current args
            context = dict(args)
            try:
                if eval(condition, {}, context):
                    required_args.append(option['name'])
            except Exception:
                # If evaluation fails, skip this condition
                continue
                
        # If condition is a callable
        elif callable(condition):
            try:
                if condition(args):
                    required_args.append(option['name'])
            except Exception:
                # If evaluation fails, skip this condition
                continue
                
        # If condition is a dict with key-value pairs
        elif isinstance(condition, dict):
            matches = True
            for key, value in condition.items():
                if args.get(key) != value:
                    matches = False
                    break
            if matches:
                required_args.append(option['name'])
                
    return required_args