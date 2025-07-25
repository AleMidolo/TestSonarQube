def get_deprecated_args(self):
    """
    返回一个包含会弃用其他选项的字典。选项来自 `self.spec_helper.iterate_option_specs()`。
    返回一个包含会弃用其他选项的字典。
    """
    deprecated_args = {}
    for option in self.spec_helper.iterate_option_specs():
        if option.get('deprecated', False):
            deprecated_args[option['name']] = option['replacement']
    return deprecated_args