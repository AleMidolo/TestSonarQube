def get_option_spec(self, command_name):
    """
    दिए गए विकल्प नाम के लिए विनिर्देश प्राप्त करता है।
    
    :param command_name: विकल्प का नाम
    :return: विकल्प का विनिर्देश
    """
    # Assuming the option specifications are stored in a dictionary
    # Example: self.options = {'command1': 'spec1', 'command2': 'spec2'}
    return self.options.get(command_name, None)