def get_deprecated_args(self):
    """
    返回一个包含会弃用其他选项的字典。选项来自 `self.spec_helper.iterate_option_specs()`。
    返回一个包含会弃用其他选项的字典。
    """
    deprecated_args = {}
    for option_spec in self.spec_helper.iterate_option_specs():
        if 'deprecated_by' in option_spec:
            deprecated_args[option_spec['name']] = option_spec['deprecated_by']
    return deprecated_args