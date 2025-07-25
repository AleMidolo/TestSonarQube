def create_complex_argument_type(self, subcommand, type_name, option_name, spec_option):
    """
    根据 `type_name` 返回 `COMPLEX_TYPES` 中对应的函数，并在输入 `(self.vars, self.defaults, self.plugin_path), subcommand, spec_option)` 后，通过 `complex_action` 返回结果。

    构建复杂参数类型

    :param subcommand: 命令名称
    :param type_name: 复杂类型名称
    :param option_name: 选项名称
    :param spec_option: 选项的具体规范
    :return: 复杂类型实例
    """
    # 假设 COMPLEX_TYPES 是一个字典，存储了复杂类型名称与对应函数的映射
    COMPLEX_TYPES = {
        'type1': lambda vars, defaults, plugin_path, subcommand, spec_option: complex_action(vars, defaults, plugin_path, subcommand, spec_option),
        'type2': lambda vars, defaults, plugin_path, subcommand, spec_option: another_complex_action(vars, defaults, plugin_path, subcommand, spec_option),
        # 可以根据需要添加更多类型
    }
    
    # 获取对应的复杂类型函数
    complex_type_func = COMPLEX_TYPES.get(type_name)
    
    if complex_type_func:
        # 调用复杂类型函数并返回结果
        return complex_type_func(self.vars, self.defaults, self.plugin_path, subcommand, spec_option)
    else:
        raise ValueError(f"Unknown complex type: {type_name}")