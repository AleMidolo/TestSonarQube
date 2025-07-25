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
    if type_name not in self.COMPLEX_TYPES:
        raise ValueError(f"Unknown complex type: {type_name}")
        
    complex_type_func = self.COMPLEX_TYPES[type_name]
    complex_args = (self.vars, self.defaults, self.plugin_path)
    
    try:
        complex_action = complex_type_func(complex_args, subcommand, spec_option)
        return complex_action
    except Exception as e:
        raise ValueError(f"Failed to create complex type {type_name} for option {option_name}: {str(e)}")