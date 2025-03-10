def get_parser_option_specs(self, command_name):
    """
    निर्दिष्ट कमांड के लिए सभी विकल्प प्राप्त करता है।

    :param command_name: कमांड का नाम (जैसे main, virsh, ospd, आदि...)
    :return: सभी कमांड विकल्पों की सूची
    """
    # Assuming self.parser is an instance of argparse.ArgumentParser or similar
    if hasattr(self, 'parser') and hasattr(self.parser, '_actions'):
        # Filter actions that are related to the specified command
        options = [action for action in self.parser._actions if command_name in action.option_strings]
        return options
    else:
        return []