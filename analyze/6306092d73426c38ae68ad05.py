def get_option_spec(self, command_name):
    """
    दिए गए विकल्प नाम के लिए विनिर्देश प्राप्त करता है।
    """
    if not hasattr(self, '_option_specs'):
        self._option_specs = {}
        
    if command_name not in self._option_specs:
        self._option_specs[command_name] = {}
        
    return self._option_specs[command_name]