def get_option_spec(self, command_name):
    """
    दिए गए विकल्प नाम के लिए विनिर्देश प्राप्त करता है।
    """
    if command_name in self.command_specs:
        return self.command_specs[command_name].get('options', {})
    return {}