def create_complex_argumet_type(self, subcommand, type_name, option_name, spec_option):
    complex_type = COMPLEX_TYPES.get(type_name)
    if complex_type is None:
        raise ValueError(f"Unknown complex type: {type_name}")
    
    complex_instance = complex_type(option_name, self.vars, self.defaults, self.plugin_path, subcommand, spec_option)
    return complex_instance.complex_action()