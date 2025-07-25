def get_option_spec(self, command_name, argument_name):
    """
    获取指定选项名称的规范。通过 `self.get_parser_option_specs()` 获取给定 `command_name` 的选项。
    获取指定选项名称的规范。
    """
    # Get all option specs for the command
    option_specs = self.get_parser_option_specs(command_name)
    
    # Search for matching argument name in option specs
    for option_spec in option_specs:
        if option_spec.get('name') == argument_name:
            return option_spec
            
    # Return None if no matching option spec found
    return None