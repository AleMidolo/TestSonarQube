def get_deprecated_args(self):
    deprecated_args = {}
    for option in self.spec_helper.iterate_option_specs():
        if option.get('deprecated'):
            deprecated_args[option['name']] = option['deprecated']
    return deprecated_args