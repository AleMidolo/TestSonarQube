def get_option_spec(self, command_name):
    """
    दिए गए विकल्प नाम के लिए विनिर्देश प्राप्त करता है।
    """
    # Assuming self.options is a dictionary where keys are command names and values are their specifications
    if command_name in self.options:
        return self.options[command_name]
    else:
        return None