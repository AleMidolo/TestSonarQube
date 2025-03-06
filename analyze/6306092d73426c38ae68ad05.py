def get_option_spec(self, command_name):
    """
    दिए गए विकल्प नाम के लिए विनिर्देश प्राप्त करता है।
    
    Args:
        command_name (str): विकल्प का नाम जिसके लिए विनिर्देश प्राप्त करना है।
    
    Returns:
        dict: विकल्प का विनिर्देश, यदि उपलब्ध हो। अन्यथा, None।
    """
    # Assuming self.options is a dictionary where keys are command names and values are their specifications
    return self.options.get(command_name, None)