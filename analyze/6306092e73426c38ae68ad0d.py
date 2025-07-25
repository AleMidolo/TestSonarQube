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
    complex_action = self.COMPLEX_TYPES.get(type_name)
    if complex_action is None:
        raise ValueError(f"Unknown complex type: {type_name}")

    return complex_action(self.vars, self.defaults, self.plugin_path, subcommand, spec_option)