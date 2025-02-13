def get_parser_option_specs(self, command_name):
    options = {
        'main': ['--help', '--version', '--verbose'],
        'virsh': ['--connect', '--list', '--start', '--shutdown'],
        'ospd': ['--config', '--log-level', '--daemon'],
    }
    return options.get(command_name, [])