def get_option_spec(self, command_name, argument_name):
    option_specs = self.get_parser_option_specs(command_name)
    return option_specs.get(argument_name, None)