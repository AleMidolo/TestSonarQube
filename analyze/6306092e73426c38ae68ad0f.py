def get_nested_custom_and_control_args(self, args):
    """
    将输入参数分为控制，嵌套和自定义参数。

    控制参数：用于控制中间表示的行为。这些参数不会被写入到规范yml文件中。  
    嵌套参数：用于Ansible playbooks，并会被写入到规范yml文件中。  
    自定义参数：自定义的Ansible变量，用于替代常规的嵌套参数使用。

    :param args: 收集到的参数列表。
    :return: (dict, dict): 扁平化的字典（control_args, nested_args）
    """
    control_args = {}
    nested_args = {}
    
    for key, value in args.items():
        if key.startswith('control_'):
            control_args[key] = value
        elif key.startswith('nested_'):
            nested_args[key] = value
        else:
            # Assuming custom args are those that don't fit the above categories
            nested_args[key] = value

    return control_args, nested_args