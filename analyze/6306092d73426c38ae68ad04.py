def get_parser_option_specs(self, command_name):
    """
    निर्दिष्ट कमांड के लिए सभी विकल्प प्राप्त करता है।

    :param command_name: कमांड का नाम (जैसे main, virsh, ospd, आदि...)
    :return: सभी कमांड विकल्पों की सूची
    """
    options = {
        'main': ['--help', '--version', '--verbose'],
        'virsh': ['--connect', '--list', '--start'],
        'ospd': ['--config', '--status', '--restart']
    }
    
    return options.get(command_name, [])