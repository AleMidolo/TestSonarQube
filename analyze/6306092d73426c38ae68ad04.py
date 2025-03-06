def get_parser_option_specs(self, command_name):
    """
    निर्दिष्ट कमांड के लिए सभी विकल्प प्राप्त करता है।

    :param command_name: कमांड का नाम (जैसे main, virsh, ospd, आदि...)
    :return: सभी कमांड विकल्पों की सूची
    """
    # Assuming self.parser_options is a dictionary where keys are command names
    # and values are lists of option specs for that command.
    if command_name in self.parser_options:
        return self.parser_options[command_name]
    else:
        return []