def get_option_spec(self, command_name):
    """
    दिए गए विकल्प नाम के लिए विनिर्देश प्राप्त करता है।
    """
    # Assuming the specifications are stored in a dictionary called `option_specs`
    if hasattr(self, 'option_specs') and command_name in self.option_specs:
        return self.option_specs[command_name]
    else:
        return None