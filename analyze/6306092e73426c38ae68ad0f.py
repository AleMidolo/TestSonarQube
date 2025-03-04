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
    custom_args = {}

    # 遍历所有参数
    for arg_name, arg_value in args.items():
        # 控制参数以_开头
        if arg_name.startswith('_'):
            control_args[arg_name] = arg_value
            
        # 自定义参数以custom_开头    
        elif arg_name.startswith('custom_'):
            custom_name = arg_name[7:] # 去掉custom_前缀
            custom_args[custom_name] = arg_value
            
        # 其他都是嵌套参数
        else:
            nested_args[arg_name] = arg_value

    # 将自定义参数合并到嵌套参数中
    nested_args.update(custom_args)

    return control_args, nested_args