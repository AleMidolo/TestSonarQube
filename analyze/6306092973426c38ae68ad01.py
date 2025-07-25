def get_deprecated_args(self):
    """
    返回一个包含会弃用其他选项的字典。选项来自 `self.spec_helper.iterate_option_specs()`。
    返回一个包含会弃用其他选项的字典。
    """
    deprecated_args = {}
    
    # 遍历所有选项规格
    for spec in self.spec_helper.iterate_option_specs():
        # 检查选项是否有弃用其他选项的设置
        if hasattr(spec, 'deprecated_options') and spec.deprecated_options:
            # 将弃用选项添加到字典中
            for deprecated_opt in spec.deprecated_options:
                deprecated_args[deprecated_opt] = spec.name
                
    return deprecated_args