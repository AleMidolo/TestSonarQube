def get_parser_option_specs(self, command_name):
    """
    निर्दिष्ट कमांड के लिए सभी विकल्प प्राप्त करता है।

    :param command_name: कमांड का नाम (जैसे main, virsh, ospd, आदि...)
    :return: सभी कमांड विकल्पों की सूची
    """
    # Assuming self.parser is an instance of argparse.ArgumentParser or similar
    if hasattr(self, 'parser') and hasattr(self.parser, '_actions'):
        options = []
        for action in self.parser._actions:
            if action.dest != 'help':  # Exclude the help option
                options.append(action.option_strings)
        return options
    else:
        return []