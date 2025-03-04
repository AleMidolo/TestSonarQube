def get_deprecated_args(self):
    """
    Returning dict with options which deprecate others.
    """
    deprecated_args = {}
    for option in self.options:
        if hasattr(option, 'deprecated_options'):
            for deprecated in option.deprecated_options:
                deprecated_args[deprecated] = option.name
    return deprecated_args